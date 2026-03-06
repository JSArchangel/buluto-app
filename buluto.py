import streamlit as st
import os
from datetime import datetime

# 1. Sayfa Ayarları
st.set_page_config(page_title="Buluto Security", layout="wide")

# 2. CSS (Net baloncuklar, Siyah plaka ve 3D butonlar)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;700&family=Lexend:wght@400;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Lexend', sans-serif !important;
    }

    /* Arka Plan: image_f95d59.png'daki orijinal mavi */
    .stApp {
        background: linear-gradient(180deg, #4facfe 0%, #00f2fe 100%);
    }
    
    /* NET BEYAZ BALONCUKLAR */
    .clear-bubble {
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 25px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
        text-align: center;
        border: 1px solid #e1e8ed;
    }

    /* KAMERA VİZÖRÜ */
    .vizor-box {
        width: 100%;
        height: 350px;
        background-color: #f8fafc;
        border-radius: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #64748b;
        border: 2px solid #e2e8f0;
    }

    /* PLAKA YAZISI - SİYAH VE FIRA CODE */
    .plaka-num {
        font-family: 'Fira Code', monospace !important;
        font-size: 52px !important;
        font-weight: 700;
        color: #000000 !important;
        letter-spacing: 4px;
        margin: 10px 0;
    }

    /* 3D BUTONLAR (image_f8f3fd.png Stili) */
    div.stButton > button {
        border-radius: 15px !important;
        font-weight: 800 !important;
        height: 60px !important;
        border: none !important;
        color: white !important;
        transition: all 0.1s !important;
    }

    /* ONAY BUTONU - Turkuaz */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {
        background: #00bcd4 !important;
        border-bottom: 6px solid #008ba3 !important;
        box-shadow: 0 4px #008ba3 !important;
    }

    /* RED BUTONU - Kırmızı */
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {
        background: #ff4b5c !important;
        border-bottom: 6px solid #d43d4c !important;
        box-shadow: 0 4px #d43d4c !important;
    }

    div.stButton > button:active {
        transform: translateY(4px) !important;
        border-bottom: 1px solid transparent !important;
        box-shadow: none !important;
    }

    header, footer, #MainMenu {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Oturum Durumu
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'active_request' not in st.session_state:
    st.session_state['active_request'] = {"Plaka": "34 BAA 001", "Saat": "05:40:12"}

# --- GİRİŞ EKRANI (Logo Dahil) ---
if not st.session_state['logged_in']:
    _, login_col, _ = st.columns([1, 1, 1])
    with login_col:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("<div class='clear-bubble'>", unsafe_allow_html=True)
        # Logo Kontrolü
        if os.path.exists("logo.png"):
            st.image("logo.png", use_container_width=True)
        else:
            st.markdown("<h2 style='color:#00bcd4;'>BULUTO</h2>", unsafe_allow_html=True)
        
        st.markdown("<p style='color:#64748b;'>Güvenli Yönetim Paneli</p>", unsafe_allow_html=True)
        u = st.text_input("Kullanıcı")
        p = st.text_input("Şifre", type="password")
        if st.button("SİSTEME GİRİŞ YAP", use_container_width=True):
            if u == "admin" and p == "buluto2024":
                st.session_state['logged_in'] = True
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- ANA PANEL ---
else:
    st.markdown("<h1 style='text-align:center; color:white; font-weight:800; margin-top:20px;'>BULUTO SECURITY</h1>", unsafe_allow_html=True)
    
    _, main_col, _ = st.columns([1, 3.5, 1])
    
    with main_col:
        # 1. Balon: Sadece Kamera (Üstteki boş balon gitti)
        st.markdown("<div class='clear-bubble'>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:12px; color:#64748b; margin-bottom:10px;'>LIVE VIDEO FEED</p>", unsafe_allow_html=True)
        st.markdown("<div class='vizor-box'>SİSTEM ANALİZ EDİLİYOR...</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # 2. Balon: Plaka Bilgisi (Yazı ve Plaka Tek Balonda)
        if st.session_state['active_request']:
            req = st.session_state['active_request']
            st.markdown("<div class='clear-bubble'>", unsafe_allow_html=True)
            st.markdown("<p style='font-size:12px; color:#64748b; margin-bottom:0;'>ALGILANAN PLAKA</p>", unsafe_allow_html=True)
            st.markdown(f"<div class='plaka-num'>{req['Plaka']}</div>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size:11px; color:#94a3b8;'>Giriş Talebi Alındı: {req['Saat']}</p>", unsafe_allow_html=True)
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

# Sidebar Test Alanı
with st.sidebar:
    if os.path.exists("logo.png"): st.image("logo.png")
    t_p = st.text_input("Plaka Simüle Et")
    if st.button("Gönder"):
        st.session_state['active_request'] = {"Plaka": t_p.upper(), "Saat": datetime.now().strftime("%H:%M:%S")}
        st.rerun()