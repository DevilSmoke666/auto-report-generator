import pytest
from app.gsheet import get_sheet_data


def test_get_sheet_data_csv(tmp_path):
    # Створюємо тимчасовий CSV файл
    csv_content = "client_name,task,status,date,comments\nJohn,Task1,Done,2025-05-01,Comment1"
    test_file = tmp_path / "test_data.csv"
    test_file.write_text(csv_content)

    # Отримуємо дані з csv
    result = get_sheet_data(csv_file=str(test_file))

    # Перевірка
    assert isinstance(result, list)
    assert isinstance(result[0], dict)
    assert result[0]["client_name"] == "John"
    assert result[0]["task"] == "Task1"
