import streamlit as st
import os
from datetime import datetime

# 1. Sayfa Ayarları
st.set_page_config(page_title="Buluto Security", layout="wide")

# 2. CSS (Sadece senin istediğin o siyah font ve TEK baloncuk)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@700&family=Lexend:wght@800&display=swap');

    html, body, [class*="css"] { font-family: 'Lexend', sans-serif !important; }

    /* Arka Plan: Orijinal Mavi */
    .stApp { background: linear-gradient(180deg, #4facfe 0%, #00f2fe 100%); }
    
    /* BEYAZ NET KUTU (Boş kutular silindi, sadece bunlar kaldı) */
    .main-card {
        background-color: white;
        border-radius: 30px;
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
        text-align: center;
    }

    /* VİZÖR (Kamera Alanı) */
    .vizor {
        width: 100%;
        height: 380px;
        background-color: #f8fafc;
        border-radius: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #94a3b8;
        border: 2px solid #f1f5f9;
    }

    /* PLAKA YAZISI - TAM SİYAH VE FIRA CODE */
    .plaka-text {
        font-family: 'Fira Code', monospace !important;
        font-size: 60px !important;
        font-weight: 700;
        color: #000000 !important;
        letter-spacing: 5px;
        margin-top: 10px;
    }

    /* 3D BUTONLAR (image_f8f3fd.png Stili) */
    div.stButton > button {
        border-radius: 20px !important;
        font-weight: 800 !important;
        height: 70px !important;
        border: none !important;
        color: white !important;
        transition: all 0.1s !important;
        font-size: 18px !important;
    }

    /* ONAYLA - Turkuaz */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {
        background: #00bcd4 !important;
        border-bottom: 7px solid #008ba3 !important;
        box-shadow: 0 4px #008ba3 !important;
    }

    /* REDDET - Kırmızı */
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {
        background: #ff4b5c !important;
        border-bottom: 7px solid #d43d4c !important;
        box-shadow: 0 4px #d43d4c !important;
    }

    div.stButton > button:active {
        transform: translateY(5px) !important;
        border-bottom: 2px solid transparent !important;
        box-shadow: none !important;
    }

    header, footer, #MainMenu {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Durum Yönetimi
if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False
if 'active_request' not in st.session_state: st.session_state['active_request'] = {"Plaka": "34 BAA 001", "Saat": "05:40:12"}

# --- GİRİŞ EKRANI (ŞİFRE VE LOGO) ---
if not st.session_state['logged_in']:
    _, login_col, _ = st.columns([1, 1.2, 1])
    with login_col:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        if os.path.exists("logo.png"):
            st.image("logo.png", use_container_width=True)
        st.markdown("<h3 style='color:#64748b; font-size:16px;'>Güvenli Yönetim Paneli</h3>", unsafe_allow_html=True)
        u = st.text_input("Yönetici")
        p = st.text_input("Şifre", type="password")
        if st.button("SİSTEME GİRİŞ YAP", use_container_width=True):
            if u == "admin" and p == "buluto2024":
                st.session_state['logged_in'] = True
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- ANA DASHBOARD ---
else:
    # Logo Sidebar'da da kalsın garanti olsun
    with st.sidebar:
        if os.path.exists("logo.png"): st.image("logo.png")
        st.markdown("---")
        t_p = st.text_input("Simülasyon Plaka")
        if st.button("Kameraya Gönder"):
            st.session_state['active_request'] = {"Plaka": t_p.upper(), "Saat": datetime.now().strftime("%H:%M:%S")}
            st.rerun()

    st.markdown("<h1 style='text-align:center; color:white; font-weight:800; margin-top:10px;'>BULUTO SECURITY</h1>", unsafe_allow_html=True)
    
    _, main_col, _ = st.columns([1, 3, 1])
    
    with main_col:
        # 1. Kutu: Sadece Video (Üstündeki boşluklar silindi!)
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.markdown("<div class='vizor'>CANLI GÖRÜNTÜ AKTARILIYOR...</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # 2. Kutu: Plaka ve Yazı BİRLEŞTİ (Altındaki boşluk silindi!)
        if st.session_state['active_request']:
            req = st.session_state['active_request']
            st.markdown("<div class='main-card'>", unsafe_allow_html=True)
            st.markdown("<p style='font-size:14px; color:#64748b; font-weight:bold; margin:0;'>ALGILANAN PLAKA</p>", unsafe_allow_html=True)
            st.markdown(f"<div class='plaka-text'>{req['Plaka']}</div>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size:12px; color:#94a3b8;'>Tespit Zamanı: {req['Saat']}</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            # 3. 3D Butonlar
            b1, b2 = st.columns(2)
            with b1:
                if st.button("✅ ONAYLA", use_container_width=True):
                    st.session_state['active_request'] = None
                    st.rerun()
            with b2:
                if st.button("❌ REDDET", use_container_width=True):
                    st.session_state['active_request'] = None
                    st.rerun()