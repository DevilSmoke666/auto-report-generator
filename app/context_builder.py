import os
from gpt_writer import generate_summary
from .utils import get_field_value
from .lang import tr  # 🧠 імпорт функції перекладу

def build_context(record, lang="ua"):
    client_name = get_field_value(record, "client_name", tr("client", lang))
    task = get_field_value(record, "task", "-")
    status = get_field_value(record, "status", "-")
    date = get_field_value(record, "date", "-")
    comments = get_field_value(record, "comments", "")

    summary_data = {
        "client": client_name,
        "task": task,
        "status": status,
        "comments": comments,
        "date": date,
    }

    summary = generate_summary(summary_data)

    # 🏷 Створюємо словник перекладів для шаблону
    labels = {
        "client": tr("client", lang),
        "task": tr("task", lang),
        "status": tr("status", lang),
        "date": tr("date", lang),
        "comments": tr("comments", lang),
        "summary": tr("summary", lang),
        "footer": tr("footer", lang)
    }

    context = {
        "title": tr("title", lang),
        "client": client_name,
        "task": task,
        "status": status,
        "summary": summary,
        "comments": comments,
        "date": date,
        "labels": labels,
        "lang": lang  # важливо для <html lang="{{ lang }}">
    }

    return context
