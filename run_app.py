
import streamlit as st
from dotenv import load_dotenv
import os

# === 🔧 КОНФІГУРАЦІЯ СТОРІНКИ Streamlit ===
st.set_page_config(page_title="AUTO-REPORT-GENERATOR", layout="centered")

# === 🎨 Web 3.0 Стилі ===
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #f7f8fc, #e5eaf5);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stTextInput>div>input {
        border: 2px solid #6c63ff;
        border-radius: 12px;
        padding: 10px;
    }
    .stButton>button {
        background-color: #6c63ff;
        color: white;
        padding: 0.6em 1.2em;
        border-radius: 8px;
        border: none;
        font-weight: bold;
        transition: background 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #5a54d6;
    }
    </style>
""", unsafe_allow_html=True)

# === 🔁 Додатковий CSS з файлу
def load_local_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# === 🔧 СЕРЕДОВИЩЕ
load_dotenv()

# === 🧩 Імпорти
from app.report_generator import generate_and_send_report
from app.ui.language_selector import select_language
from app.lang import tr


def main():
    # === 🌍 Вибір мови
    lang = select_language()

    # === 🧾 Заголовок
    st.markdown(f"## 📝 {tr('title', lang)}")
    st.markdown(f"### {tr('generate_report', lang)}")

    # === 📥 Джерело даних
    data_source = st.radio(tr("data_source", lang), ["Google Sheet ID", tr("upload_csv", lang)])
    sheet_id = None
    csv_file = None

    if data_source == "Google Sheet ID":
        sheet_id = st.text_input(tr("enter_sheet_id", lang))
    else:
        csv_file = st.file_uploader(tr("upload_csv", lang), type=["csv"])

    email = st.text_input(tr("enter_email", lang))

    # === 🚀 Кнопка генерації
    if st.button(tr("generate_button", lang)):
        if not email:
            st.warning(tr("missing_email", lang))
        elif not sheet_id and not csv_file:
            st.warning(tr("missing_source", lang))
        else:
            with st.spinner(tr("generating", lang)):
                try:
                    generate_and_send_report(email=email, sheet_id=sheet_id, csv_file=csv_file)
                    st.success(f"✅ {tr('report_sent', lang)}: {email}")
                except Exception as e:
                    st.error(f"❌ {tr('error_generating', lang)}: {str(e)}")

# === 🚀 Запуск
if __name__ == "__main__":
    load_local_css("app/ui/styles.css")  # виклик всередині if __name__
    main()
