"""
عطرسان — نسخه‌ی نمایشی فارسی برای اجرا در Streamlit
Atrsan — Persian demo of the storefront, packaged for Streamlit.

Run:
    pip install -r requirements.txt
    streamlit run app.py
"""
from pathlib import Path

import streamlit as st

SITE = Path(__file__).parent / "atrsan_fa.html"

st.set_page_config(
    page_title="عطرسان",
    page_icon="🌹",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide all of Streamlit's own interface so only the website is visible,
# filling the whole browser window.
st.markdown(
    """
    <style>
      #MainMenu, footer, header, [data-testid="stToolbar"], [data-testid="stHeader"],
      [data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"],
      [data-testid="stDecoration"], [data-testid="stStatusWidget"] {display: none !important;}
      html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        overflow: hidden !important; background: #F1ECE4;}
      .block-container, [data-testid="stMainBlockContainer"] {
        padding: 0 !important; margin: 0 !important; max-width: 100% !important;}
      [data-testid="stVerticalBlock"] {gap: 0 !important;}
      iframe {display: block; width: 100vw !important; height: 100vh !important; border: 0 !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = SITE.read_text(encoding="utf-8")

if hasattr(st, "iframe"):
    st.iframe(html, height=900)
else:  # older Streamlit versions
    import streamlit.components.v1 as components

    components.html(html, height=900, scrolling=True)
