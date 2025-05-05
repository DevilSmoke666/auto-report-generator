# app/ui/language_selector.py

import streamlit as st

# 🟢 Підтримувані мови
LANGUAGES = {
    "Українська": "ua",
    "English": "en"
}

# 🔵 Основна функція
def select_language() -> str:
    # 🧠 Вибір мови користувачем
    lang_choice = st.sidebar.selectbox(
        "🌐 Оберіть мову / Select language",
        list(LANGUAGES.keys())
    )
    # 🔁 Повертаємо код мови ("uk" або "en")
    return LANGUAGES[lang_choice]
