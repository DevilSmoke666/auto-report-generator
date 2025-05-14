import streamlit as st
import os
from dotenv import load_dotenv

# === 🖥️ Налаштування сторінки ===
st.set_page_config(page_title="AUTO-REPORT-GENERATOR", layout="centered")

# === 🌿 Середовище ===
load_dotenv()

# === 📦 Імпорти ===
from app.report_generator import generate_and_send_report
from app.ui.language_selector import select_language
from app.ui.theme_selector import select_theme
from app.lang import tr

# === 🎨 Завантаження теми з themes.css ===
def load_theme_css(theme):
    try:
        with open("app/ui/themes.css") as f:
            css = f.read()
            selected = f"body.{theme}"
            start = css.find(selected)
            if start != -1:
                end = css.find("body.", start + 1)
                part = css[start:end] if end != -1 else css[start:]
                st.markdown(f"<style>{part}</style>", unsafe_allow_html=True)
            else:
                st.warning(f"⚠️ Theme '{theme}' not found in themes.css.")
    except FileNotFoundError:
        st.error("❌ Файл themes.css не знайдено.")

# === 🚀 Головна логіка ===
def main():
    # === 🌍 Мова
    lang = select_language()

    # === 🎨 Тема
    theme = select_theme(lang)
    load_theme_css(theme)

    # === 🧾 Заголовок
    st.markdown(f"<h1 class='title'>{tr('title', lang)}</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3 class='subtitle'>{tr('generate_report', lang)}</h3>", unsafe_allow_html=True)

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

# === 🔁 Запуск
if __name__ == "__main__":
    main()
