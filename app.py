"""
عطرسان — نسخه‌ی نمایشی فارسی برای اجرا در Streamlit
Atrsan — Persian demo of the storefront, packaged for Streamlit.

Run:
    pip install -r requirements.txt
    streamlit run app.py
"""
from pathlib import Path

import streamlit as st

HERE = Path(__file__).parent
SITE = HERE / "atrsan_fa.html"

st.set_page_config(
    page_title="عطرسان · نسخه‌ی نمایشی",
    page_icon="🌹",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Hide Streamlit's own chrome so the demo looks like a real website,
# and make the sidebar right-to-left for Persian text.
st.markdown(
    """
    <style>
      #MainMenu, footer, header [data-testid="stToolbar"] {visibility: hidden;}
      header {background: transparent !important;}
      .block-container {padding: 0.6rem 0.6rem 0 0.6rem !important; max-width: 100% !important;}
      section[data-testid="stSidebar"] * {direction: rtl; text-align: right;
        font-family: Tahoma, "Vazirmatn", sans-serif;}
      section[data-testid="stSidebar"] code {direction: ltr; display: inline-block;}
      iframe {border: 1px solid #D9D0C3; border-radius: 6px; background: #F1ECE4;}
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data
def load_site() -> str:
    return SITE.read_text(encoding="utf-8")


with st.sidebar:
    st.markdown("## عطرسان")
    st.caption("نسخه‌ی نمایشی فروشگاه · داده‌ها نمونه هستند و پرداخت واقعی انجام نمی‌شود.")

    st.markdown("### مسیر پیشنهادی نمایش")
    st.markdown(
        """
**۱. خانه:** طراحی هنری، بطری‌های تولیدشده و دود متحرک.

**۲. یافتن عطر:** در کادر جستجو بنویسید:
«عطر شیرین با وانیل و عود» · «گل رز بدون عود» · «یه چیز تمیز و تازه برای تابستون» · «شبیه یلدا ولی سبک‌تر»

**۳. آزمون:** به ۸ سؤال جواب دهید و تیپ عطری خود را ببینید.

**۴. صفحه‌ی محصول:** هرم نت‌ها، نمودار شخصیت و عطرهای مشابه.

**۵. مقایسه:** چند عطر را با دکمه‌ی «مقایسه» کنار هم بگذارید.

**۶. آتلیه:** عطر اختصاصی خود را مرحله‌به‌مرحله بسازید.

**۷. سبد و پرداخت:** کد تخفیف `ATRSAN10` را امتحان کنید (درگاه پرداخت شبیه‌سازی است).

**۸. استودیو (مدیریت):** داشبورد فروش، سفارش‌ها، انبار، مشتریان و نقش‌های کاربری.
        """
    )

    st.markdown("### تنظیمات نمایش")
    height = st.slider("ارتفاع پنجره‌ی سایت (پیکسل)", 600, 1600, 900, 50)
    mobile = st.toggle("نمایش در اندازه‌ی موبایل", value=False)

    st.download_button(
        "دانلود فایل سایت (HTML)",
        data=load_site(),
        file_name="atrsan_fa.html",
        mime="text/html",
        help="این فایل را بدون اینترنت هم می‌توانید با مرورگر باز کنید.",
        use_container_width=True,
    )
    st.caption("تمام فونت‌ها داخل فایل قرار دارند؛ برای نمایش، اتصال اینترنت لازم نیست.")

html = load_site()


def show_site(width=None):
    """Embed the site; uses st.iframe on new Streamlit, components.html on older versions."""
    if hasattr(st, "iframe"):
        st.iframe(html, height=height, width=width or "stretch")
    else:
        import streamlit.components.v1 as components

        components.html(html, height=height, scrolling=True, width=width)


if mobile:
    left, mid, right = st.columns([1, 1.1, 1])
    with mid:
        show_site(width=400)
else:
    show_site()
