import json
import os
import streamlit as st

# Page Configuration - سائیڈ بار کو موبائل پر بند رکھنے کے لیے
st.set_page_config(
    page_title="SCS Cosmetics (ASMA)",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom Styling
st.markdown(
    """
    <style>
    .main-title { text-align: center; color: #fff; font-weight: bold; }
    .stTextInput > div > div > input { background-color: #2b2b2b; color: white; }
    </style>
""",
    unsafe_allow_html=True,
)

# Admin Password Protection
st.sidebar.markdown("### 🔐 Admin Panel / ایڈمن پینل")
password = st.sidebar.text_input(
    "پاسورڈ درج کریں (صرف ایڈمن کے لیے)", type="password"
)
ADMIN_PASSWORD = "Khizar asma"

is_admin = False
if password:
  if password == ADMIN_PASSWORD:
    st.sidebar.success("✅ پاسورڈ درست ہے! آپ ایڈمن موڈ میں ہیں۔")
    is_admin = True
  else:
    st.sidebar.error(" براہ کرم درست پاسورڈ درج کریں۔")

# File to store product data permanently
DATA_FILE = "products.json"


def load_products():
  if os.path.exists(DATA_FILE):
    try:
      with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
    except:
      return []
  return []


def save_products(products):
  with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(products, f, ensure_ascii=False, indent=4)


# ----------------- ADMIN PRODUCT UPLOAD SYSTEM -----------------
if is_admin:
  st.markdown(
      "### 🛠️ Admin Dashboard: Add New Product / نئی پروڈکٹ شامل کریں"
  )
  with st.form("product_form", clear_on_submit=True):
    p_name = st.text_input("پروڈکٹ کا نام (Product Name)")
    p_desc = st.text_area("تفصیل (Description)")
    p_price = st.text_input("قیمت (Price in IQD)")
    p_image = st.file_uploader(
        "پروڈکٹ کی تصویر اپلوڈ کریں (Upload Image)", type=["jpg", "png", "jpeg"]
    )
    submit_button = st.form_submit_button(label="پروڈکٹ لائیو کریں")

    if submit_button:
      if p_name and p_price:
        image_path = None
        if p_image is not None:
          os.makedirs("uploaded_images", exist_ok=True)
          image_path = os.path.join("uploaded_images", p_image.name)
          with open(image_path, "wb") as f:
            f.write(p_image.getbuffer())

        new_product = {
            "name": p_name,
            "description": p_desc,
            "price": p_price,
            "image_path": image_path,
        }

        products = load_products()
        products.append(new_product)
        save_products(products)
        st.success(f"پروڈکٹ '{p_name}' کامیابی کے ساتھ لائیو کر دی گئی ہے!")
      else:
        st.warning("براہ کرم کم از کم پروڈکٹ کا نام اور قیمت درج کریں۔")
  st.markdown("---")

# ----------------- DISPLAY PRODUCTS SECTION -----------------
st.markdown("### 🛍️ Available Products / پروڈکٹس")

products = load_products()

if not products:
  st.info(
      "فی الحال کوئی پروڈکٹ موجود نہیں ہے۔ ایڈمن پینل سے نئی پروڈکٹ شامل"
      " کریں۔"
  )
else:
  for idx, prod in enumerate(products):
    col1, col2 = st.columns([2, 1])
    with col1:
      st.markdown(f"#### {prod['name']}")
      st.markdown(f"{prod['description']}")
      st.markdown(f"*قیمت:* {prod['price']} IQD")
      st.markdown(
          f"[🛒 واٹس ایپ پر آرڈر"
          f" کریں](https://wa.me/9647864607927?text=Hi,%20I%20want%20to%20order%20{prod['name']})"
      )

    with col2:
      if prod["image_path"] and os.path.exists(prod["image_path"]):
        st.image(prod["image_path"], use_column_width=True)
      else:
        st.info("تصویر دستیاب نہیں")

    if idx < len(products) - 1:
      st.markdown("---")

st.markdown("---")

# Official Link Section for Admin
if is_admin:
  st.markdown("### 🔗 ٹک ٹاک بائیو اور شیئرنگ کے لیے آفیشل لنک")
  st.markdown(
      "یہ آپ کی ایپ کا لائیو لنک ہے۔ اسماء یہاں سے کاپی کر کے ٹک ٹاک بائیو میں"
      " لگائے گی:"
  )
  st.code("https://asma-scs-cosmetics.streamlit.app", language="text")
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
