"""Shared helper: show one self-contained HTML page full-screen, with Streamlit's own UI hidden."""
from pathlib import Path

import streamlit as st

HERE = Path(__file__).parent

HIDE_STREAMLIT = """
<style>
  #MainMenu, footer, header, [data-testid="stToolbar"], [data-testid="stHeader"],
  [data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"], [data-testid="stSidebarNav"],
  [data-testid="stDecoration"], [data-testid="stStatusWidget"] {display: none !important;}
  html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
    overflow: hidden !important; background: #F1ECE4;}
  .block-container, [data-testid="stMainBlockContainer"] {
    padding: 0 !important; margin: 0 !important; max-width: 100% !important;}
  [data-testid="stVerticalBlock"] {gap: 0 !important;}
  iframe {display: block; width: 100vw !important; height: 100vh !important;
    height: 100dvh !important; border: 0 !important;}
</style>
"""


def show_page(filename: str, title: str) -> None:
    st.set_page_config(page_title=title, page_icon="🌹", layout="wide",
                       initial_sidebar_state="collapsed")
    st.markdown(HIDE_STREAMLIT, unsafe_allow_html=True)
    html = (HERE / filename).read_text(encoding="utf-8")
    if hasattr(st, "iframe"):
        st.iframe(html, height=900)
    else:  # older Streamlit versions
        import streamlit.components.v1 as components
        components.html(html, height=900, scrolling=True)
