import streamlit as st
import pandas as pd
from datetime import datetime
import os

# 1. Sayfa Konfigürasyonu
st.set_page_config(page_title="Buluto Pro | Smart Security", layout="wide")

# 2. ÖZEL TEMA VE FONT (Modern Lexend Font & Vibrant Blue Gradient)
st.markdown("""
    <style>
    /* Google Fonts Import */
    @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;600;800&display=swap');

    /* Genel Font ve Arka Plan */
    html, body, [class*="css"]  {
        font-family: 'Lexend', sans-serif !important;
    }

    .stApp {
        background: linear-gradient(180deg, #4facfe 0%, #00f2fe 50%, #1e3c72 100%);
        color: #ffffff;
    }
    
    /* Buzlu Cam Kart Tasarımı (Daha Yumuşak ve Şık) */
    .glass-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.25);
        border-radius: 30px;
        padding: 35px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        text-align: center;
    }

    /* Kamera Vizörü */
    .camera-viewport {
        width: 100%;
        max-width: 800px;
        aspect-ratio: 16/9;
        margin: 0 auto;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 25px;
        border: 2px solid rgba(255, 255, 255, 0.3);
        display: flex;
        justify-content: center;
        align-items: center;
        font-weight: 300;
        letter-spacing: 2px;
    }

    /* Plaka Tasarımı (Modern ve Temiz) */
    .plaka-box {
        font-size: 56px;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: 6px;
        margin: 20px 0;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }

    /* Butonlar (Apple Tarzı) */
    div.stButton > button {
        background: #ffffff !important;
        color: #1e3c72 !important;
        border: none !important;
        border-radius: 20px !important;
        height: 4em !important;
        font-weight: 600 !important;
        font-size: 16px !important;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1) !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    }
    div.stButton > button:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.2) !important;
    }

    /* Gereksiz Streamlit Elemanlarını Gizle */
    header, footer, #MainMenu {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Oturum Durumu
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'active_request' not in st.session_state:
    st.session_state['active_request'] = {"Plaka": "34 BAA 001", "Saat": "02:26:30"}

# --- GİRİŞ EKRANI ---
if not st.session_state['logged_in']:
    c1, c2, c3 = st.columns([1, 1.2, 1])
    with c2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        if os.path.exists("logo.png"):
            st.image("logo.png", use_container_width=True)
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<h2 style='font-weight:800; margin-bottom:30px;'>Hoş Geldiniz</h2>", unsafe_allow_html=True)
        u = st.text_input("Yönetici Kimliği")
        p = st.text_input("Giriş Anahtarı", type="password")
        if st.button("SİSTEMİ BAŞLAT", use_container_width=True):
            if u == "admin" and p == "buluto2024":
                st.session_state['logged_in'] = True
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- ANA DASHBOARD ---
else:
    # Üst Navigasyon (Ferah)
    st.markdown(f"""
    <div style="display: flex; justify-content: space-between; padding: 25px 50px;">
        <div style="font-weight: 800; font-size: 22px; letter-spacing: 1px;">BULUTO SECURITY <span style="font-weight:300; opacity:0.7;">PRO</span></div>
        <div style="font-weight: 600; background: rgba(255,255,255,0.2); padding: 5px 20px; border-radius: 30px;">
            ● CANLI YAYIN AKTİF
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_l, col_m, col_r = st.columns([1, 4, 1])
    
    with col_m:
        # Kamera Kartı
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<div class='camera-viewport'>CANLI GÖRÜNTÜ YÜKLENİYOR...</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # Karar Kartı (Plaka Odaklı)
        if st.session_state['active_request']:
            req = st.session_state['active_request']
            st.markdown(f"""
            <div class='glass-card'>
                <p style='font-size: 14px; text-transform: uppercase; letter-spacing: 3px; opacity: 0.8;'>Algılanan Plaka</p>
                <div class='plaka-box'>{req['Plaka']}</div>
                <p style='font-size: 14px; opacity: 0.7;'>Giriş Talebi Alındı: {req['Saat']}</p>
                <br>
            </div>
            """, unsafe_allow_html=True)
            
            b_c1, b_c2 = st.columns(2)
            if b_c1.button("✅ ONAYLA VE KAPIYI AÇ", use_container_width=True):
                st.balloons()
                st.session_state['active_request'] = None
            if b_c2.button("❌ GİRİŞİ ENGELLE", use_container_width=True):
                st.session_state['active_request'] = None
                st.rerun()

    # Alt Bilgi
    st.markdown(f"<p style='text-align: center; opacity: 0.5; font-size: 12px; margin-top: 50px;'>© 2026 Buluto Smart Systems • {datetime.now().strftime('%d.%m.%Y')}</p>", unsafe_allow_html=True)

    # Simülasyon
    with st.sidebar:
        st.markdown("### Araç Test Paneli")
        t_p = st.text_input("Plaka Gir")
        if st.button("Kameraya Gönder"):
            st.session_state['active_request'] = {"Plaka": t_p.upper(), "Saat": datetime.now().strftime("%H:%M:%S")}
            st.rerun()