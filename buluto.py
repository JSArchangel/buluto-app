import streamlit as st
import os
from datetime import datetime
import time

# 1. Sayfa Konfigürasyonu
st.set_page_config(
    page_title="Buluto Security Pro",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS MASTER - Animasyonlu Bulutlar ve Modern Tema
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@700&family=Lexend:wght@800&display=swap');

    /* Sayfa Geneli ve Hareketli Arkaplan */
    html, body, [class*="css"] { 
        font-family: 'Lexend', sans-serif !important; 
    }
    
    .stApp { 
        background: linear-gradient(180deg, #00c6ff 0%, #0072ff 100%);
        overflow: hidden;
    }

    /* BULUT ANİMASYONU KATMANLARI */
    .stApp::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 200%; height: 100%;
        background: url('https://www.transparenttextures.com/patterns/clouds.png');
        opacity: 0.3;
        animation: moveClouds 60s linear infinite;
        pointer-events: none;
    }

    @keyframes moveClouds {
        from { transform: translateX(0); }
        to { transform: translateX(-50%); }
    }

    /* ÜST BOŞLUKLARI SIFIRLAMA */
    [data-testid="stHeader"] { display: none !important; }
    header { visibility: hidden !important; height: 0px !important; }
    .main .block-container {
        padding-top: 0px !important;
        margin-top: -30px !important;
    }

    /* Glassmorphism Kartları - Daha Saydam ve Şık */
    .glass-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(15px);
        border-radius: 25px;
        padding: 30px;
        margin-bottom: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        text-align: center;
    }

    /* Video Vizörü */
    .video-container {
        width: 100%;
        height: 350px;
        background: #0f172a;
        border-radius: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #38bdf8;
        border: 2px solid rgba(56, 189, 248, 0.5);
    }

    /* Plaka Tasarımı - Neon Efekti Artırıldı */
    .plaka-bg {
        background: #0f172a; 
        border-radius: 15px;
        padding: 20px;
        margin: 15px auto;
        border: 2px solid #38bdf8;
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.4);
    }
    .plaka-num {
        font-family: 'Fira Code', monospace !important;
        font-size: 55px !important;
        font-weight: 700;
        color: #ffffff !important;
        letter-spacing: 8px;
        text-shadow: 0 0 10px #38bdf8;
    }

    /* Butonlar */
    div.stButton > button {
        border-radius: 15px !important;
        font-weight: 800 !important;
        height: 60px !important;
        border: none !important;
        color: white !important;
        transition: 0.3s;
    }
    
    /* Onay Butonu (Yeşilimsi/Mavi) */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {
        background: linear-gradient(45deg, #00f2fe 0%, #4facfe 100%) !important;
        box-shadow: 0 4px 15px rgba(0, 242, 254, 0.4);
    }
    
    /* Red Butonu (Mercan) */
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {
        background: linear-gradient(45deg, #ff5f6d 0%, #ffc371 100%) !important;
        box-shadow: 0 4px 15px rgba(255, 95, 109, 0.4);
    }

    div.stButton > button:hover { transform: scale(1.02); }

    /* Input Alanları */
    .stTextInput input {
        background: rgba(255, 255, 255, 0.2) !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        color: white !important;
        border-radius: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Session State
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'active_request' not in st.session_state:
    st.session_state['active_request'] = {"Plaka": "34 BAA 001", "Saat": "05:40:12"}
if 'history' not in st.session_state:
    st.session_state['history'] = []

# --- GİRİŞ EKRANI ---
if not st.session_state['logged_in']:
    _, login_col, _ = st.columns([1, 1.2, 1])
    with login_col:
        st.markdown("<div style='margin-top: 80px;'></div>", unsafe_allow_html=True)
        if os.path.exists("logo.png"):
            st.image("logo.png", use_container_width=True)
        
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("### 🔐 Yönetici Erişimi")
        user = st.text_input("Kullanıcı Adı")
        pw = st.text_input("Şifre", type="password")
        if st.button("SİSTEMİ AKTİVE ET", use_container_width=True):
            if user == "admin" and pw == "buluto2024":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("Giriş Başarısız!")
        st.markdown("</div>", unsafe_allow_html=True)

# --- ANA PANEL ---
else:
    st.markdown("<h1 style='text-align:center; color:white; font-weight:900; letter-spacing:3px;'>BULUTO SECURITY PRO</h1>", unsafe_allow_html=True)
    
    with st.sidebar:
        if os.path.exists("logo.png"): st.image("logo.png")
        st.markdown("---")
        if st.button("Güvenli Çıkış", use_container_width=True):
            st.session_state['logged_in'] = False
            st.rerun()

    _, main_col, _ = st.columns([1, 2.5, 1])
    with main_col:
        # Kamera Alanı
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<p style='color:#38bdf8; font-weight:bold;'>🔵 CANLI ANALİZ SİSTEMİ</p>", unsafe_allow_html=True)
        st.markdown("<div class='video-container'>YAYIN BEKLENİYOR...</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # Tespit Alanı
        if st.session_state['active_request']:
            req = st.session_state['active_request']
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            st.markdown("<div class='plaka-bg'><div class='plaka-num'>" + req['Plaka'] + "</div></div>", unsafe_allow_html=True)
            st.write(f"⏱ **Tespit Zamanı:** {req['Saat']}")
            
            b1, b2 = st.columns(2)
            with b1:
                if st.button("✅ GİRİŞİ ONAYLA", use_container_width=True):
                    st.session_state['history'].append(req)
                    st.session_state['active_request'] = None
                    st.rerun()
            with b2:
                if st.button("❌ ERİŞİMİ REDDET", use_container_width=True):
                    st.session_state['active_request'] = None
                    st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)