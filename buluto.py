import streamlit as st
import os
from PIL import Image

# 1. Sayfa Ayarları
st.set_page_config(page_title="Buluto Security", page_icon="☁️", layout="centered")

# 2. Arka Plan ve Stil (Senin logonun net görünmesi için fonu ayarladık)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: white; }
    .login-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding-top: 20px;
    }
    .stButton>button {
        width: 100%;
        background-color: #1E90FF;
        color: white;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="login-container">', unsafe_allow_html=True)

# 3. LOGOYU GÖSTERME (En garanti yol)
current_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(current_dir, "logo.png")

if os.path.exists(logo_path):
    image = Image.open(logo_path)
    st.image(image, width=400)
else:
    st.error(f"HATA: logo.png bulunamadı! Aranan yol: {logo_path}")

# Giriş Formu
st.title("BULUTO SECURITY")
user = st.text_input("Kullanıcı Adı")
pw = st.text_input("Şifre", type="password")

if st.button("Sisteme Güvenli Giriş Yap"):
    if user == "admin" and pw == "buluto2024":
        st.success("Giriş Başarılı!")
        st.balloons()
    else:
        st.error("Hatalı kullanıcı adı veya şifre!")

st.markdown('</div>', unsafe_allow_html=True)