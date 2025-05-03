import streamlit as st
from dotenv import load_dotenv
import os
import sys

# Завантаження .env
load_dotenv()

# Імпорти з app/
from app.report_generator import generate_and_send_report
from app.UI.language_selector import select_language
from app.lang import tr

def main():
    # ОБОВʼЯЗКОВО першим streamlit-командою
    st.set_page_config(page_title="AUTO-REPORT-GENERATOR", layout="centered")

    lang = select_language()

    st.title("📄 " + tr("title", lang))
    st.markdown(tr("generate_report", lang))

    data_source = st.radio(tr("data_source", lang), ["Google Sheet ID", "CSV файл"])
    sheet_id = None
    csv_file = None

    if data_source == "Google Sheet ID":
        sheet_id = st.text_input(tr("enter_sheet_id", lang))
    else:
        csv_file = st.file_uploader(tr("upload_csv", lang), type=["csv"])

    email = st.text_input(tr("enter_email", lang))

    if st.button(tr("generate_button", lang)):
        if not email:
            st.warning(tr("missing_email", lang))
        elif not sheet_id and not csv_file:
            st.warning(tr("missing_source", lang))
        else:
            st.spinner(tr("generating", lang))
            try:
                generate_and_send_report(email=email, sheet_id=sheet_id, csv_file=csv_file)
                st.success(f"✅ {tr('report_sent', lang)}: {email}")
            except Exception as e:
                st.error(f"❌ {tr('error_generating', lang)}: {str(e)}")

if __name__ == "__main__":
    main()
