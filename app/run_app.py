import streamlit as st
from dotenv import load_dotenv
import sys


from app.report_generator import generate_and_send_report  # ✅ Абсолютний імпорт

load_dotenv()


def main():
    st.set_page_config(page_title="AUTO-REPORT-GENERATOR", layout="centered")
    st.title("📋 AUTO-REPORT-GENERATOR")
    st.markdown("Згенеруйте звіт 🧾 і отримаєте його на email 📩")

    data_source = st.radio("Оберіть джерело даних:", ["Google Sheet ID", "CSV файл"])
    sheet_id = None
    csv_file = None

    if data_source == "Google Sheet ID":
        sheet_id = st.text_input("Введіть Google Sheet ID:")
    else:
        csv_file = st.file_uploader("Завантажте CSV файл", type=["csv"])

    email = st.text_input("Введіть email клієнта:")

    if st.button("🚀 Згенерувати та надіслати звіт"):
        if not email:
            st.warning("Будь ласка, введіть email")
        elif not sheet_id and not csv_file:
            st.warning("Введіть Google Sheet ID або завантажте CSV")
        else:
            with st.spinner("Генеруємо звіт..."):
                try:
                    generate_and_send_report(email=email, sheet_id=sheet_id, csv_file=csv_file)
                    st.success(f"✅ Звіт надіслано на {email}")
                except Exception as e:
                    st.error(f"❌ Помилка: {e}")


if __name__ == "__main__":
    main()
