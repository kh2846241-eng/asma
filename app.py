import json
import os
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="SCS Cosmetics (ASMA)",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom Styling (خوبصورت پنک تھیم، پھول اور ڈیزائن)
st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        color: #ff4d94;
        font-weight: 800;
        font-size: 32px;
        text-shadow: 1px 1px 3px rgba(255, 105, 180, 0.3);
    }
    .sub-title {
        text-align: center;
        color: #ff80b3;
        font-size: 16px;
        margin-bottom: 20px;
    }
    .flower-banner {
        text-align: center;
        font-size: 22px;
        margin-bottom: 10px;
    }
    .product-card {
        background: linear-gradient(145deg, #1e1e24, #2a2228);
        border: 1px solid #ff4d94;
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(255, 77, 148, 0.15);
    }
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        background-color: #2b222a;
        color: white;
        border: 1px solid #ff80b3;
    }
    .order-btn {
        display: inline-block;
        background-color: #25D366;
        color: white !important;
        padding: 8px 16px;
        border-radius: 20px;
        text-decoration: none;
        font-weight: bold;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Admin Password Protection
st.sidebar.markdown("### 🔐 Admin Panel / ایڈمن پینل")
password = st.sidebar.text_input(
    "پاسورڈ درج کریں (صرف ایڈمن کے لیے)", type="password"
)
ADMIN_PASSWORD = "KHIZARجان"

is_admin = False
if password:
  if password == ADMIN_PASSWORD:
    st.sidebar.success("✅ پاسورڈ درست ہے! آپ ایڈمن موڈ میں ہیں۔")
    is_admin = True
  else:
    st.sidebar.error("❌ غلط پاسورڈ! براہ کرم درست پاسورڈ درج کریں۔")

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


# Header with floral cosmetics aesthetic
st.markdown(
    "<div class='flower-banner'>🌸 🌺 🌷 💐 🌷 🌺 🌸</div>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h1 class='main-title'>✨ SCS Cosmetics (ASMA) ✨</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p class='sub-title'>💖 Pure & Natural Skincare | حسن، نکھار اور قدرتی خوبصورتی"
    " کا راز 💖</p>",
    unsafe_allow_html=True,
)
st.markdown(
    "<div class='flower-banner'>🌸 🌹 🌺 🌿 🌺 🌹 🌸</div>",
    unsafe_allow_html=True,
)
st.markdown("---")

# ----------------- ADMIN DASHBOARD -----------------
if is_admin:
  st.markdown(
      "### 🛠️ Admin Dashboard: Add New Product / نئی پروڈکٹ لگائیں"
  )
  with st.form("product_form", clear_on_submit=True):
    p_name = st.text_input("پروڈکٹ کا نام (Product Name)")
    p_desc = st.text_area("تفصیل (Description)")
    p_price = st.text_input("قیمت (Price in IQD)")
    p_image = st.file_uploader(
        "پروڈکٹ کی تصویر اپلوڈ کریں (Upload Image)", type=["jpg", "png", "jpeg"]
    )
    submit_button = st.form_submit_button(label="🌸 پروڈکٹ لائیو کریں")

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

        prods = load_products()
        prods.append(new_product)
        save_products(prods)
        st.success(f"پروڈکٹ '{p_name}' کامیابی کے ساتھ لائیو کر دی گئی ہے!")
        st.rerun()
      else:
        st.warning("براہ کرم کم از کم پروڈکٹ کا نام اور قیمت درج کریں۔")
  st.markdown("---")

# ----------------- DISPLAY & MANAGE PRODUCTS -----------------
st.markdown("### 🛍️ Available Products / ہماری پروڈکٹس 🌷")

products = load_products()

if not products:
  st.info(
      "فی الحال کوئی پروڈکٹ موجود نہیں ہے۔ ایڈمن پینل سے نئی پروڈکٹ شامل"
      " کریں۔"
  )
else:
  for idx, prod in enumerate(products):
    st.markdown("<div class='product-card'>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 1])

    with col1:
      st.markdown(f"### 🌸 {prod['name']}")
      st.write(f"📝 {prod.get('description', '')}")
      st.markdown(f"*💰 قیمت:* {prod['price']} IQD")
      order_link = f"https://wa.me/9647864607927?text=Hi,%20I%20want%20to%20order%20{prod['name']}"
      st.markdown(
          f"<a href='{order_link}' class='order-btn' target='_blank'>🛒 واٹس ایپ"
          " پر آرڈر کریں</a>",
          unsafe_allow_html=True,
      )

    with col2:
      if prod.get("image_path") and os.path.exists(prod["image_path"]):
        st.image(prod["image_path"], use_column_width=True)
      else:
        st.caption("تصویر دستیاب نہیں ہے")

    # اگر ایڈمن لاگ ان ہو تو پروڈکٹ ایڈٹ اور ڈیلیٹ کرنے کے اختیارات
    if is_admin:
      with st.expander(
          f"⚙️ Manage / تبدیل یا ختم کریں ({prod['name']})", expanded=False
      ):
        edit_name = st.text_input(
            "نیا نام درج کریں", value=prod["name"], key=f"edit_name_{idx}"
        )
        edit_desc = st.text_area(
            "نئی تفصیل درج کریں",
            value=prod.get("description", ""),
            key=f"edit_desc_{idx}",
        )
        edit_price = st.text_input(
            "نئی قیمت درج کریں (IQD)",
            value=prod["price"],
            key=f"edit_price_{idx}",
        )

        col_save, col_del = st.columns(2)
        with col_save:
          if st.button("💾 تبدیلی محفوظ کریں (Save)", key=f"save_btn_{idx}"):
            products[idx]["name"] = edit_name
            products[idx]["description"] = edit_desc
            products[idx]["price"] = edit_price
            save_products(products)
            st.success("تبدیلی محفوظ ہو گئی!")
            st.rerun()

        with col_del:
          if st.button(
              "🗑️ پروڈکٹ ڈیلیٹ کریں (Remove)",
              key=f"del_btn_{idx}",
              type="primary",
          ):
            # اگر تصویر موجود ہو تو لوکل فائل سے بھی مٹا دے
            if prod.get("image_path") and os.path.exists(prod["image_path"]):
              try:
                os.remove(prod["image_path"])
              except:
                pass
            products.pop(idx)
            save_products(products)
            st.warning("پروڈکٹ کامیابی سے ڈیلیٹ ہو گئی!")
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# Footer & Admin Direct Link
if is_admin:
  st.markdown("### 🔗 ٹک ٹاک بائیو کا لنک")
  st.code("https://asma-scs-cosmetics.streamlit.app", language="text")
  st.markdown("---")

st.markdown(
    """
    <div style='text-align: center; color: #ff80b3; font-size: 13px;'>
        🌸 Developed & Secured with Love for SCS Cosmetics 🌸<br>
        واتس ایپ / رابطہ: 9647864607927+ 🇮🇶 | كربلاء، العراق
    </div>
    """,
    unsafe_allow_html=True,
)
