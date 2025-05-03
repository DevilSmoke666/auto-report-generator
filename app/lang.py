# === 📁 Файл: app/lang.py ===

TRANSLATIONS = {
    "ua": {
        "title": "Автоматичний звіт",
        "client": "Клієнт",
        "task": "Задача",
        "status": "Статус",
        "date": "Дата",
        "comments": "Коментарі",
        "summary": "Висновок",
    },
    "en": {
        "title": "Automatic Report",
        "client": "Client",
        "task": "Task",
        "status": "Status",
        "date": "Date",
        "comments": "Comments",
        "summary": "Summary",
    },
}

def tr(key: str, lang: str = "ua") -> str:
    return TRANSLATIONS.get(lang, {}).get(key, key)
