# python -m streamlit run app.py
# streamlit run app.py
# python -m streamlit run pages/login.py


import streamlit as st

st.set_page_config(
    page_title="TAKTIK | تكتيك",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.switch_page("pages/login.py")

