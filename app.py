import os
import streamlit as st

# Page Configuration - سائیڈ بار کو موبائل پر ڈیفالٹ بند رکھنے کے لیے
st.set_page_config(
    page_title="SCS Cosmetics (ASMA)",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom Styling (CSS)
st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        color: #fff;
        font-weight: bold;
    }
    .stTextInput > div > div > input {
        background-color: #2b2b2b;
        color: white;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Admin Password Protection in Sidebar
st.sidebar.markdown("### 🔐 Admin Panel / ایڈمن پینل")
password = st.sidebar.text_input(
    "پاسورڈ درج کریں (صرف ایڈمن کے لیے)", type="password"
)

# Define Admin Password
ADMIN_PASSWORD = "KHIZARجان"
is_admin = password == ADMIN_PASSWORD

# App Header
st.markdown(
    "<h1 class='main-title'>🌸 SCS Cosmetics (ASMA) 🌸</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #ff99cc;'>Pure & Natural Skincare | خوبصورتی اور قدرتی نکھار کا بہترین راز</p>",
    unsafe_allow_html=True,
)
st.markdown("---")

# Products Section
st.markdown("### 🛍️ Available Products / پروڈکٹس")

# Product 1: Anti-Melasma Gel
col1, col2 = st.columns(2)
with col1:
    st.markdown("#### Anti-Melasma Gel")
    st.markdown("پگمنٹیشن اور چھائیوں کے لیے بہترین جیل")
    st.markdown("*قیمت:* 1920 IQD")
    st.markdown(
        "[🛒 واٹس ایپ پر آرڈر کریں](https://wa.me/9647864607927?text=Hi,%20I%20want%20to%20order%20Anti-Melasma%20Gel)"
    )

with col2:
    # تصویر کے پاتھ کا درست طریقہ
    if os.path.exists("gel.jpg"):
        st.image("gel.jpg", use_column_width=True)
    else:
        st.info("تصویر دستیاب نہیں (gel.jpg)")

st.markdown("---")

# Product 2: Rose Face Wash
col3, col4 = st.columns(2)
with col3:
    st.markdown("#### Rose Face Wash")
    st.markdown("روز فیس واش / جلد کی گہرائی سے صفائی")
    st.markdown("*قیمت:* 960 IQD")
    st.markdown(
        "[🛒 واٹس ایپ پر آرڈر کریں](https://wa.me/9647864607927?text=Hi,%20I%20want%20to%20order%20Rose%20Face%20Wash)"
    )

with col4:
    if os.path.exists("facewash.jpg"):
        st.image("facewash.jpg", use_column_width=True)
    else:
        st.info("تصویر دستیاب نہیں (facewash.jpg)")

st.markdown("---")

# Admin Section (Visible only when correct password is entered)
if is_admin:
    st.success("✅ آپ ایڈمن مود (Admin Mode) میں داخل ہو چکے ہیں!")
    st.markdown("---")
    st.markdown("### 🔗 ٹک ٹاک بائیو اور شیئرنگ کے لیے آفیشل لنک")
    st.markdown(
        "یہ آپ کی ایپ کا لائیو لنک ہے۔ اسماء یہاں سے لنک کاپی کر کے ٹک ٹاک بائیو میں لگایا کرے گی[span_2](start_span)[span_2](end_span)[span_3](start_span)[span_3](end_span):"
    )

    # Official Permanent Live Link Box
    st.code("https://asma-scs-cosmetics.streamlit.app", language="text")

    st.markdown(
        "💡 اس لنک پر عام کسٹمرز کے لیے کوئی پاسورڈ نہیں ہوگا، وہ براہ راست چیزیں دیکھ کر واٹس ایپ پر آرڈر کریں گے۔"
    )
    st.markdown("---")

# Footer
st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 12px;'>
        Developed & Secured by Software & Cybersecurity Expert 💻<br>
        واتس ایپ / رابطہ: 9647864607927+ 🇮🇶 | مقيم و شاغل في كربلاء، العراق
    </div>
    """,
    unsafe_allow_html=True,
)
