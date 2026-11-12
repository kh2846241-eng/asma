import streamlit as st
import json
import os
import base64

# صفحہ کی سیٹنگ
st.set_page_config(
    page_title="ASMA - SCS Cosmetics Official Store",
    page_icon="🌸",
    layout="wide"
)

# ڈیٹا سیو کرنے کی فائل اور فولڈر
DATA_FILE = "asma_products.json"
UPLOAD_DIR = "uploaded_images"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

def load_products():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except:
                return []
    return [
        {"id": 1, "name": "روز فیس واش / Rose Face Wash", "price": "960 روپے", "desc": "جلد کو گہرائی تک صاف کرے، نم اور تازہ رکھے.", "img": "https://placehold.co/300x300/ffb6c1/ffffff?text=Rose+Face+Wash"},
        {"id": 2, "name": "اینٹی میلزمہ جیل / Anti-Melasma Gel", "price": "1920 روپے", "desc": "سیاہ دھبوں اور میلزمہ کے نشانات کو نمایاں طور پر کم کرتا ہے.", "img": "https://placehold.co/300x300/dda0dd/ffffff?text=Anti-Melasma+Gel"}
    ]

def save_products(products):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

products = load_products()

# کسٹم سٹائلنگ
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Amiri', serif;
        direction: rtl;
        text-align: right;
    }
    .main-header {
        background: linear-gradient(135deg, #8b0000, #ff69b4, #dda0dd);
        padding: 30px;
        border-radius: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        border: 2px solid #ffd700;
        margin-bottom: 25px;
        position: relative;
    }
    .product-card {
        background: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(255, 182, 193, 0.4);
        border: 1px solid #ffb6c1;
        text-align: center;
        margin-bottom: 20px;
    }
    .stButton>button {
        background: linear-gradient(to right, #ff1493, #ff69b4);
        color: white;
        border-radius: 12px;
        font-weight: bold;
        border: none;
        padding: 10px 20px;
        width: 100%;
    }
    .dev-badge {
        background-color: #f8f9fa;
        border-top: 2px dashed #ffb6c1;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-top: 40px;
        font-size: 14px;
        color: #444;
    }
    </style>
""", unsafe_allow_html=True)

# سیشن سٹیٹ فار لاگ ان
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# سائیڈ بار (لاگ ان پینل)
st.sidebar.markdown("### 🔐 اسما کا لاگ ان / Admin Panel")
admin_pass = st.sidebar.text_input("پاسورڈ درج کریں", type="password")

if admin_pass == "Khizar jaan":
    st.session_state.logged_in = True
    st.sidebar.success("✅ خوش آمدید اسما جی!")
elif admin_pass and admin_pass != "Khizar jaan":
    st.sidebar.error("❌ غلط پاسورڈ!")

# --- مین ہیڈر ---
st.markdown("""
    <div class="main-header">
        <div style="position: absolute; top: 15px; left: 20px; background: rgba(0,0,0,0.3); padding: 5px 12px; border-radius: 20px; font-size: 13px; color: #fffacd; border: 1px solid rgba(255,255,255,0.2);">
            📞 رابطہ: +964 7864607927 | 🇮🇶 عراق
        </div>
        <h1 style="font-size: 45px; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">🌸 اسما (ASMA) - SCS Cosmetics 🌸</h1>
        <p style="font-size: 20px; margin-top: 10px;">خوبصورتی اور قدرتی نکھار کا بہترین راز | Pure & Natural Skincare</p>
        <p style="font-size: 14px; color: #fffacd;">Success Chaser Store & Dream Stars Team Official Partner</p>
    </div>
""", unsafe_allow_html=True)

# اگر اسما لاگ ان ہے تو وہ گیلری سے تصویر اپ لوڈ کر کے پروڈکٹ ایڈ کر سکے گی
if st.session_state.logged_in:
    st.markdown("---")
    st.markdown("### 🛠️ ایڈمن پینل: گیلری سے تصویر منتخب کریں اور نئی پروڈکٹ شامل کریں")
    
    with st.form("add_product_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            p_name = st.text_input("پروڈکٹ کا نام")
            p_price = st.text_input("قیمت (مثلاً: 960 روپے)")
        with col2:
            # گیلری سے ڈائریکٹ تصویر اٹھانے کا فائل اپلوڈر بٹن
            img_file = st.file_uploader("گیلری سے پروڈکٹ کی تصویر منتخب کریں (Browse)", type=["jpg", "jpeg", "png"])
            
        p_desc = st.text_area("تفصیل (Description)")
        
        submit_btn = st.form_submit_button("✨ پروڈکٹ ایپ میں شائع کریں")
        
        if submit_btn:
            if p_name and p_price and img_file is not None:
                # تصویر کو فولڈر میں محفوظ کرنا
                img_path = os.path.join(UPLOAD_DIR, img_file.name)
                with open(img_path, "wb") as f:
                    f.write(img_file.getbuffer())
                
                new_id = products[-1]["id"] + 1 if products else 1
                new_item = {
                    "id": new_id,
                    "name": p_name,
                    "price": p_price,
                    "desc": p_desc,
                    "img": img_path
                }
                products.append(new_item)
                save_products(products)
                st.success("🎉 پروڈکٹ کامیابی سے شامل ہو گئی ہے!")
                st.rerun()
            else:
                st.warning("⚠️ براہ کرم نام، قیمت اور گیلری سے تصویر لازمی منتخب کریں۔")

    if products:
        st.markdown("#### 🗑️ موجودہ پروڈکٹ کو حذف کریں")
        del_id = st.selectbox("حذف کرنے کے لیے پروڈکٹ منتخب کریں", [p['id'] for p in products], format_func=lambda x: next(p['name'] for p in products if p['id'] == x))
        if st.button("اس پروڈکٹ کو ہٹائیں"):
            products = [p for p in products if p['id'] != del_id]
            save_products(products)
            st.success("🗑️ پروڈکٹ ہٹا دی گئی ہے!")
            st.rerun()
    st.markdown("---")

# --- پبلک کیٹلاگ ---
st.markdown("### 🛍️ تمام دستیاب پروڈکٹس اور ڈیلز")

search_query = st.text_input("🔍 پروڈکٹ تلاش کریں...", "")
filtered_products = [p for p in products if search_query.lower() in p['name'].lower() or search_query.lower() in p['desc'].lower()]

if not filtered_products:
    st.info("کوئی پروڈکٹ موجود نہیں ہے۔")
else:
    cols = st.columns(3)
    for index, product in enumerate(filtered_products):
        with cols[index % 3]:
            # چیک کریں کہ تصویر فولڈر کی ہے یا لنک
            img_src = product['img']
            st.markdown(f"""
                <div class="product-card">
                    <img src="{img_src}" style="width:100%; height:200px; object-fit:cover; border-radius:10px; margin-bottom:10px;" onerror="this.onerror=null; this.src='https://placehold.co/300x300/ffb6c1/ffffff?text=SCS+Product';">
                    <h4 style="color: #8b0000; margin-bottom: 5px;">{product['name']}</h4>
                    <p style="color: #ff1493; font-weight: bold; font-size: 18px; margin-bottom: 5px;">{product['price']}</p>
                    <p style="color: #555; font-size: 14px; min-height: 40px;">{product['desc']}</p>
                </div>
            """, unsafe_allow_html=True)
            
            wa_text = f"السلام علیکم، مجھے یہ پروڈکٹ آرڈر کرنی ہے: {product['name']} (قیمت: {product['price']})"
            st.markdown(f"""
                <a href="https://wa.me/923087669078?text={wa_text}" target="_blank">
                    <button style="background-color: #25d366; color: white; border: none; padding: 10px; border-radius: 10px; width: 100%; font-weight: bold; cursor: pointer;">
                        🛒 واٹس ایپ پر آرڈر کریں
                    </button>
                </a>
            """, unsafe_allow_html=True)

# --- لنک شیئرنگ سیکشن ---
st.markdown("---")
st.markdown("""
    <div style="background-color: #fff0f5; padding: 25px; border-radius: 15px; border: 2px dashed #ff1493; text-align: center; margin-top: 30px;">
        <h3 style="color: #c71585; margin-bottom: 10px;">📌 ٹک ٹاک بائیو اور شیئرنگ کے لیے آفیشل لنک</h3>
        <p style="color: #333; font-size: 16px;">یہ آپ کی ایپ کا لائیو لنک ہے۔ اسما یہاں سے لنک دیکھ کر یا کاپی کر کے ٹک ٹاک بائیو میں لگایا کرے گی:</p>
        <p style="background: #fff; padding: 12px; border-radius: 8px; border: 1px solid #ffb6c1; font-weight: bold; color: #8b0000; font-size: 16px; display: inline-block; width: 90%;">
            🔗 https://asma-scs-cosmetics.streamlit.app <span style="font-size: 12px; color: #555; display:block;">(جب آپ اسے لائیو کریں گے تو یہی لنک ایکٹو ہو جائے گا)</span>
        </p>
        <p style="color: #666; font-size: 13px; margin-top: 10px;">💡 اس لنک پر عام کسٹمرز کے لیے کوئی پاسورڈ نہیں ہوگا، وہ براہ راست چیزیں دیکھ کر واٹس ایپ پر آرڈر کریں گے۔</p>
    </div>
""", unsafe_allow_html=True)

# --- ڈویلپر کریڈٹ ---
st.markdown("""
    <div class="dev-badge">
        <p style="margin: 0; font-weight: bold; color: #8b0000;">💻 Developed & Secured by Software & Cybersecurity Expert</p>
        <p style="margin: 5px 0 0 0; color: #555;">کیا آپ کو بھی اپنی بزنس ویب سائٹ، ای کامرس ایپ یا ایڈوانسڈ سیکیورٹی سسٹمز بنوانے ہیں؟ آج ہی رابطہ کریں!</p>
        <p style="margin: 5px 0 0 0; font-weight: bold; color: #2e8b57;">📞 واٹس ایپ / رابطہ: +964 7864607927 &nbsp;|&nbsp; 🇮🇶 مقیم و شاغل في كربلاء، العراق</p>
    </div>
""", unsafe_allow_html=True)