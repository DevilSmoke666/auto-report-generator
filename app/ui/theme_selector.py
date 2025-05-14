import streamlit as st
from app.lang import tr

def select_theme(lang: str) -> str:
    if "theme" not in st.session_state:
        st.session_state["theme"] = "light"

    with st.sidebar:
        st.markdown(f"### 🌈 {tr('interface_theme', lang)}")
        theme = st.radio(
            "",
            ["light", "dark"],
            index=0 if st.session_state["theme"] == "light" else 1
        )
        st.session_state["theme"] = theme

    # ✅ Додай це: вставка JS через iframe-safe метод
    st.components.v1.html(f"""
        <script>
            const body = window.parent.document.querySelector('body');
            if (body) {{
                body.classList.remove('light', 'dark');
                body.classList.add("{st.session_state['theme']}");
            }}
        </script>
    """, height=0)

    return st.session_state["theme"]
