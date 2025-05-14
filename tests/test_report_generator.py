# tests/test_report_generator.py
import pytest
from pathlib import Path # Для типу tmp_path, хоча pytest передає його автоматично
# from unittest.mock import ANY # Може знадобитися для assert_called_with

# Припускаючи, що generate_and_send_report імпортується так:
from app.report_generator import generate_and_send_report

# Проста мок-функція для перекладу, щоб зробити тест незалежним від реальних файлів локалізації
# і консистентним з тим, як ми тестували build_context.
def mock_translate_simple(key, lang="ua", **kwargs):
    """Проста мок-функція для імітації перекладу."""
    # Спрощені переклади, достатні для цього тесту
    if key == "client":
        return f"ПерекладенийКлієнт_{lang}" # Відповідає очікуванням у тесті
    # Для інших ключів, які можуть бути потрібні для labels в context_arg_for_pdf
    # (якщо build_context їх генерує і вони використовуються в назві файлу PDF)
    # можна додати більше логіки сюди, або просто повернути заглушку.
    return f"tr_{key}_{lang}"

def test_generate_and_send_report_csv(tmp_path: Path, mocker): # Додаємо mocker
    """
    Тестує generate_and_send_report з CSV файлом,
    мокуючи всі зовнішні залежності та API-виклики.
    """
    # 0. Готуємо тестові дані (один запис у CSV)
    csv_file_path: Path = tmp_path / "test_input.csv"
    # Використовуємо ключ 'client_record_key' у CSV, щоб продемонструвати,
    # що context['client'] буде результатом tr('client', lang) з build_context,
    # оскільки build_context шукає 'client_name' у record.
    csv_content = "client_record_key,task,status,date,comments\nClientA,TaskB,StatusC,2024-05-15,SomeComment"
    csv_file_path.write_text(csv_content, encoding="utf-8")

    test_email_recipient = "a@b.com"

    # 1. Мокуємо залежності
    
    # Мокуємо 'tr' та 'generate_summary' всередині 'app.context_builder'
    mocker.patch('app.context_builder.tr', side_effect=mock_translate_simple)
    mocked_generate_summary = mocker.patch('app.context_builder.generate_summary')
    mocked_generate_summary.return_value = "Фіктивне резюме для звіту."
    
    # Мокуємо функції, які викликаються безпосередньо з app.report_generator
    mocked_get_sheet_data = mocker.patch('app.report_generator.get_sheet_data')
    mocked_generate_pdf = mocker.patch('app.report_generator.generate_pdf')
    mocked_zip_reports = mocker.patch('app.report_generator.zip_reports')
    mocked_send_email = mocker.patch('app.report_generator.send_email')
    
    mocked_makedirs = mocker.patch('os.makedirs')

    # 2. Викликаємо функцію, що тестується
    generate_and_send_report(email=test_email_recipient, csv_file=str(csv_file_path))

    # 3. Перевіряємо, що наші мок-функції були викликані правильно

    mocked_get_sheet_data.assert_not_called()
    mocked_generate_summary.assert_called_once() 
    mocked_generate_pdf.assert_called_once()
    
    args_gp, _ = mocked_generate_pdf.call_args
    context_arg_for_pdf = args_gp[0]
    filename_arg_for_pdf = args_gp[1]

    expected_client_in_context = mock_translate_simple("client", "ua")
    assert context_arg_for_pdf['client'] == expected_client_in_context
    assert str(filename_arg_for_pdf).endswith(f"report_1_{expected_client_in_context}.pdf")

    mocked_zip_reports.assert_called_once()
    args_zr, _ = mocked_zip_reports.call_args
    assert len(args_zr[0]) == 1 
    assert str(args_zr[0][0]).endswith(f"report_1_{expected_client_in_context}.pdf")
    assert str(args_zr[1]).startswith("all_reports_")

    # --- ВИПРАВЛЕНА ЧАСТИНА ДЛЯ mocked_send_email ---
    mocked_send_email.assert_called_once()
    actual_call_args_send_email = mocked_send_email.call_args 
    
    # Перевіряємо позиційний аргумент (zip_name)
    assert str(actual_call_args_send_email.args[0]).startswith("all_reports_") 
    
    # Перевіряємо іменований аргумент (recipient)
    assert actual_call_args_send_email.kwargs['recipient'] == test_email_recipient
    # --- КІНЕЦЬ ВИПРАВЛЕНОЇ ЧАСТИНИ ---

    mocked_makedirs.assert_called()
