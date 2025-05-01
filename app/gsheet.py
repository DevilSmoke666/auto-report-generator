import os
import gspread
import pandas as pd
from typing import List, Dict, Optional
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials

from app.config import SERVICE_ACCOUNT_PATH  # 🔥 новий імпорт

load_dotenv()

# Область доступу до Google Sheets API
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Значення за замовчуванням
DEFAULT_SHEET_NAME = os.getenv("GOOGLE_SHEET_ID", "SEO-Звіт")


def init_gsheet():
    """
    Ініціалізує авторизований клієнт GSpread.
    """
    if not SERVICE_ACCOUNT_PATH:
        raise ValueError("SERVICE_ACCOUNT_PATH не задано у .env або config.py")
    creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_PATH, SCOPE)
    return gspread.authorize(creds)


def get_sheet_data(sheet_id: Optional[str] = None, csv_file: Optional[str] = None) -> List[Dict]:
    """
    Отримує дані з Google Sheets або CSV-файлу.

    :param sheet_id: Google Sheet ID (опціонально)
    :param csv_file: шлях до CSV-файлу (опціонально)
    :return: список словників з даними
    """
    if csv_file:
        df = pd.read_csv(csv_file)
        return df.to_dict(orient="records")

    sheet_id = sheet_id or DEFAULT_SHEET_NAME
    client = init_gsheet()
    sheet = client.open_by_key(sheet_id).sheet1
    return sheet.get_all_records()


def add_new_lead(client_name: str, task: str, status: str, date: str, comments: str) -> None:
    """
    Додає новий рядок у таблицю
    """
    client = init_gsheet()
    sheet = client.open_by_key(DEFAULT_SHEET_NAME).sheet1
    sheet.append_row([client_name, task, status, date, comments])
