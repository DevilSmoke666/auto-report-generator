# tests/test_pdf_generator.py
from pathlib import Path # Переконайтеся, що цей імпорт є, якщо ви типізуєте tmp_path
from app.pdf_generator import generate_pdf # Переконайтеся, що імпорт правильний

def test_generate_pdf(tmp_path: Path):
    """
    Тестує генерацію PDF, надаючи повний очікуваний контекст, включаючи 'labels'.
    """
    context = {
        'title': 'Test Report Title PDF', # Назва звіту
        'client': 'Client X Name',      # Ім'я клієнта для тіла звіту
        'task': 'Task Y Description',   # Опис завдання
        'status': 'Done Status',        # Статус
        'date': '2024-01-01',           # Дата
        'comments': 'All good comments for PDF.', # Коментарі
        'summary': 'Final result summary for PDF.',# Резюме
        # === ОСЬ КЛЮЧОВИЙ МОМЕНТ: ДОДАЙТЕ СЛОВНИК 'labels' ===
        'labels': {
            'client': 'Мітка Клієнт:',             # Текстова мітка для поля "клієнт"
            'task': 'Мітка Завдання:',             # Текстова мітка для поля "завдання"
            'status': 'Мітка Статус:',             # Текстова мітка для поля "статус"
            'date': 'Мітка Дата:',                 # Текстова мітка для поля "дата"
            'comments': 'Мітка Коментарі:',         # Текстова мітка для поля "коментарі"
            'summary': 'Мітка Резюме:',            # Текстова мітка для поля "резюме"
            'footer': 'Мітка Підвал Звіту'         # Якщо ваш шаблон використовує labels.footer
            # Додайте сюди всі ключі, які ваш report_template.html 
            # очікує всередині об'єкта {{ labels.* }}
        },
        'lang': 'ua' # Якщо ваш HTML-шаблон використовує <html lang="{{ lang }}">
    }
    
    # tmp_path надається pytest і є об'єктом Path
    output_path = tmp_path / "report_for_test.pdf"
    
    generate_pdf(context, str(output_path))

    assert output_path.exists(), "PDF файл не було створено"
    assert output_path.stat().st_size > 0, "PDF файл порожній"
