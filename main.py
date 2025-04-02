from gsheet import get_sheet_data
from pdf_generator import generate_pdf
from email_sender import send_email
import os
import shutil

# Отримуємо всі записи з Google Таблиці
data = get_sheet_data()
os.makedirs("reports", exist_ok=True)

# Генеруємо PDF-звіти
for i, record in enumerate(data):
    client_name = record.get("Ім'я клієнта", "Невідомо")
    task = record.get("Задача", "-")
    status = record.get("Статус", "-")
    date = record.get("Дата", "-")
    comments = record.get("Коментарі", "")

    context = {
        "title": "Автоматичний звіт",
        "client": client_name,
        "task": task,
        "status": status,
        "summary": f"{task} для клієнта {client_name} {status.lower()}.",
        "comments": comments,
        "date": date,
    }

    output_path = f"reports/report_{i+1}_{client_name}.pdf"
    generate_pdf(context, output_path)
    print(f"[✓] Звіт збережено: {output_path}")

# Створюємо ZIP-архів
shutil.make_archive("all_reports", "zip", "reports")
print("[✓] Архів створено: all_reports.zip")

# Надсилаємо звіти на email
send_email("all_reports.zip")
