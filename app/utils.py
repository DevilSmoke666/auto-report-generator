### Файл: app/utils.py

FIELD_MAP = {
    "client_name": ["client_name", "Ім'я клієнта", "Client", "Клієнт"],
    "task": ["task", "Задача", "Завдання"],
    "status": ["status", "Статус"],
    "date": ["date", "Дата"],
    "comments": ["comments", "Коментарі"],
    "amount": ["amount", "Сума", "Ціна", "Price"]
}

def get_field_value(record: dict, field_key: str, default: str = "-") -> str:
    """
    Шукає значення за ключем, з підтримкою багатомовності.
    :param record: рядок з таблиці
    :param field_key: поле у FIELD_MAP
    :param default: значення за скочуванням, якщо не знайдено
    """
    for key in FIELD_MAP.get(field_key, []):
        if key in record and record[key]:
            return str(record[key]).strip()
    return default
