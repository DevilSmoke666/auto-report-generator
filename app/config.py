import os
from dotenv import load_dotenv

load_dotenv()

# Google Sheets
SERVICE_ACCOUNT_PATH = os.getenv("SERVICE_ACCOUNT_PATH", "app/config/credentials.json")
print("➡️ SERVICE_ACCOUNT_PATH =", SERVICE_ACCOUNT_PATH)

# Gmail JSON (опціонально, якщо колись потрібно)
GMAIL_CREDENTIALS_PATH = os.getenv("GMAIL_CREDENTIALS_PATH", "app/config/gmail_credentials.json")

# SMTP налаштування
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")
EMAIL_TO = os.getenv("EMAIL_TO")
