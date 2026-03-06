import streamlit as st
import pandas as pd
from datetime import datetime
import os

# 1. Sayfa Yapılandırması
st.set_page_config(page_title="Buluto | Pro Security Dashboard", layout="wide")

# 2. ÖZEL TEMA (Deep Blue Modern UI)
st.markdown("""
    <style>
    /* Ana Arka Plan - Derin Lacivert Gradyan */
    .stApp {
        background: linear-gradient(180deg, #020024 0%, #090979 45%, #0052D4 100%);
        color: #ffffff;
    }
    
    /* Buzlu Cam (Glassmorphism) Kart Tasarımı */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 25px;
        padding: 30px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-bottom: 25px;
    }

    /* Kamera Vizörü (Koyu ve şık) */
    .camera-viewport {
        width: 100%;
        max-width: 750px;
        aspect-ratio: 16/9;
        margin: 0 auto;
        background: rgba(0, 0, 0, 0.4);
        border-radius: 20px;
        border: 1px solid rgba(30, 144, 255, 0.3);
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* Plaka Yazı Tipi (Modern Monospace) */
    .plaka-box {
        font-family: 'JetBrains Mono', 'Courier New', monospace;
        font-size: 42px;
        font-weight: 800;
        color: #00D4FF;
        text-shadow: 0 0 15px rgba(0, 212, 255, 0.5);
        letter-spacing: 5px;
    }

    /* Modern Butonlar */
    div.stButton > button {
        background: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 15px !important;
        height: 3.5em !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    div.stButton > button:hover {
        background: rgba(0, 212, 255, 0.2) !important;
        border-color: #00D4FF !important;
        transform: scale(1.02);
    }

    /* Streamlit Gereksizleri Gizle */
    header, footer, #MainMenu {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Oturum Durumu
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'active_request' not in st.session_state:
    st.session_state['active_request'] = {"Plaka": "34 PRO 2024", "Saat": "05:45"}

# --- GİRİŞ EKRANI ---
if not st.session_state['logged_in']:
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        if os.path.exists("logo.png"):
            st.image("logo.png", width=300)
        st.markdown("<div class='glass-card' style='text-align:center;'>", unsafe_allow_html=True)
        st.markdown("<h3>Güvenli Erişim</h3>", unsafe_allow_html=True)
        u = st.text_input("Kimlik")
        p = st.text_input("Şifre", type="password")
        if st.button("SİSTEME GİRİŞ YAP", use_container_width=True):
            if u == "admin" and p == "buluto2024":
                st.session_state['logged_in'] = True
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- ANA PANEL ---
else:
    # Üst Navigasyon
    st.markdown("""
    <div style="display: flex; justify-content: space-between; padding: 20px 40px; background: rgba(0,0,0,0.2); margin-bottom: 20px;">
        <div style="font-weight: bold; color: #00D4FF; letter-spacing: 2px;">BULUTO SECURITY PRO</div>
        <div style="font-family: monospace;">● LIVE_FEED_01 | ACTIVE</div>
    </div>
    """, unsafe_allow_html=True)

    # Merkezi Alan
    col_l, col_m, col_r = st.columns([1, 4, 1])
    
    with col_m:
        # Kamera Kartı
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 14px; color: #888;'>CAM_FRONT_ENTRANCE</p>", unsafe_allow_html=True)
        st.markdown("<div class='camera-viewport'><p style='color: #444;'>VIDEO YÜKLENİYOR...</p></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # Karar Kartı
        if st.session_state['active_request']:
            req = st.session_state['active_request']
            st.markdown(f"""
            <div class='glass-card' style='text-align: center;'>
                <span style='color: #888; font-size: 12px;'>ALGILANAN PLAKA</span>
                <div class='plaka-box'>{req['Plaka']}</div>
                <hr style='border: 0.5px solid rgba(255,255,255,0.1); margin: 20px 0;'>
                <div style='display: flex; justify-content: space-around;'>
                    <div style='color: #00ff00; font-size: 14px;'>Giriş İsteği Alındı</div>
                    <div style='color: #888; font-size: 14px;'>Saat: {req['Saat']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            b_c1, b_c2 = st.columns(2)
            if b_c1.button("✅ ONAYLA VE KAPIYI AÇ", use_container_width=True):
                st.balloons()
                st.session_state['active_request'] = None
            if b_c2.button("❌ GİRİŞİ ENGELLE", use_container_width=True):
                st.warning("Giriş engellendi.")
                st.session_state['active_request'] = None

    # Alt Simülasyon Paneli
    with st.sidebar:
        st.markdown("### Sistem Araçları")
        test_p = st.text_input("Simüle Plaka")
        if st.button("Araç Gönder"):
            st.session_state['active_request'] = {"Plaka": test_p.upper(), "Saat": datetime.now().strftime("%H:%M")}
            st.rerun()