# -*- coding: utf-8 -*-
TRANSLATIONS = {
    "ua": {
        "title": "Автоматичний звіт",
        "generate_report": "Згенерувати звіт",
        "data_source": "Джерело даних",
        "generate_button": "Генерувати",
        "enter_sheet_id": "Введіть Google Sheet ID",
        "upload_csv": "Завантажте CSV файл",
        "enter_email": "Введіть email",
        "missing_email": "Будь ласка, введіть email",
        "missing_source": "Вкажіть sheet_id або завантажте CSV",
        "generating": "Генеруємо...",
        "report_sent": "Звіт надіслано",
        "error_generating": "Помилка генерації",
        "client": "Клієнт",
        "task": "Задача",
        "status": "Статус",
        "date": "Дата",
        "comments": "Коментарі",
        "summary": "Висновок"
    },
    "en": {
        "title": "Automatic Report",
        "generate_report": "Generate Report",
        "data_source": "Data Source",
        "generate_button": "Generate",
        "enter_sheet_id": "Enter Google Sheet ID",
        "upload_csv": "Upload CSV file",
        "enter_email": "Enter email",
        "missing_email": "Please enter an email",
        "missing_source": "Specify sheet_id or upload CSV",
        "generating": "Generating...",
        "report_sent": "Report sent",
        "error_generating": "Error while generating",
        "client": "Client",
        "task": "Task",
        "status": "Status",
        "date": "Date",
        "comments": "Comments",
        "summary": "Summary"
    }
}
def tr(key: str, lang: str = "ua") -> str:
    return TRANSLATIONS.get(lang, {}).get(key, key)
