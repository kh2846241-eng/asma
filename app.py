import os
import streamlit as st

# Page Configuration
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

# Password Validation Logic
if password:
  if password == ADMIN_PASSWORD:
    st.sidebar.success("✅ پاسورڈ درست ہے! آپ ایڈمن موڈ میں ہیں۔")
    is_admin = True
  else:
    st.sidebar.error("❌ غلط پاسورڈ! براہ کرم درست پاسورڈ درج کریں۔")
    is_admin = False
else:
  is_admin = False

# ----------------- ADMIN PRODUCT UPLOAD SYSTEM -----------------
if is_admin:
  st.markdown(
      "### 🛠️ Admin Dashboard: Add New Product / نئی پروڈکٹ شامل کریں"
  )
  with st.form("product_form"):
    p_name = st.text_input("پروڈکٹ کا نام (Product Name)")
    p_desc = st.text_area("تفصیل (Description)")
    p_price = st.text_input("قیمت (Price in IQD)")
    p_image = st.file_uploader(
        "پروڈکٹ کی تصویر اپلوڈ کریں (Upload Image)", type=["jpg", "png", "jpeg"]
    )
    submit_button = st.form_submit_button(
        label="پروڈکٹ لائیو کریں (Save Product)"
    )

    if submit_button:
      if p_name and p_price:
        if p_image is not None:
          os.makedirs("uploaded_images", exist_ok=True)
          img_path = os.path.join("uploaded_images", p_image.name)
          with open(img_path, "wb") as f:
            f.write(p_image.getbuffer())
          st.success(
              f"پروڈکٹ '{p_name}' اور تصویر کامیابی کے ساتھ محفوظ ہو گئی ہے!"
          )
        else:
          st.success(f"پروڈکٹ '{p_name}' کامیابی کے ساتھ محفوظ ہو گئی ہے!")
      else:
        st.warning("براہ کرم کم از کم پروڈکٹ کا نام اور قیمت درج کریں۔")
  st.markdown("---")

# ----------------- DISPLAY PRODUCTS SECTION -----------------
st.markdown("### 🛍️ Available Products / پروڈکٹس")

col1, col2 = st.columns(2)
with col1:
  st.markdown("#### Anti-Melasma Gel")
  st.markdown("پگمنٹیشن اور چھائیوں کے لیے بہترین جیل")
  st.markdown("*قیمت:* 1920 IQD")
  st.markdown(
      "[🛒 واٹس ایپ پر آرڈر"
      " کریں](https://wa.me/9647864607927?text=Hi,%20I%20want%20to%20order%20Anti-Melasma%20Gel)"
  )

with col2:
  if os.path.exists("gel.jpg"):
    st.image("gel.jpg", use_column_width=True)
  else:
    st.info("تصویر دستیاب نہیں (gel.jpg)")

st.markdown("---")

col3, col4 = st.columns(2)
with col3:
  st.markdown("#### Rose Face Wash")
  st.markdown("روز فیس واش / جلد کی گہرائی سے صفائی")
  st.markdown("*قیمت:* 960 IQD")
  st.markdown(
      "[🛒 واٹس ایپ پر آرڈر"
      " کریں](https://wa.me/9647864607927?text=Hi,%20I%20want%20to%20order%20Rose%20Face%20Wash)"
  )

with col4:
  if os.path.exists("facewash.jpg"):
    st.image("facewash.jpg", use_column_width=True)
  else:
    st.info("تصویر دستیاب نہیں (facewash.jpg)")

st.markdown("---")

if is_admin:
  st.markdown("### 🔗 ٹک ٹاک بائیو اور شیئرنگ کے لیے آفیشل لنک")
  st.markdown(
      "یہ آپ کی ایپ کا لائیو لنک ہے۔ اسماء یہاں سے لنک کاپی کر کے ٹک ٹاک بائیو میں"
      " لگایا کرے گی:"
  )
  st.code("https://asma-scs-cosmetics.streamlit.app", language="text")
  st.markdown(
      "💡 *اس لنک پر عام کسٹمرز کے لیے کوئی پاسورڈ نہیں ہوگا، وہ براہ راست چیزیں"
      " دیکھ کر واٹس ایپ پر آرڈر کریں گے۔*"
  )
  st.markdown("---")

st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 12px;'>
        Developed & Secured by Software & Cybersecurity Expert 💻<br>
        واتس ایپ / رابطہ: 9647864607927+ 🇮🇶 | مقيم و شاغل في كربلاء، العراق
    </div>
    """,
    unsafe_allow_html=True,
)
