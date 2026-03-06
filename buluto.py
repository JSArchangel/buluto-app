import streamlit as st
import pandas as pd
from datetime import datetime
import os

# 1. Sayfa Konfigürasyonu
st.set_page_config(page_title="Buluto Pro | Smart Security", layout="wide")

# 2. ÖZEL TEMA (Logo Alanı Eklenmiş Balon Tasarım)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;600;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Lexend', sans-serif !important;
    }

    .stApp {
        background: linear-gradient(135deg, #00d2ff 0%, #3a7bd5 100%);
        color: #1e3c72;
    }
    
    /* Balon Kart Yapısı */
    .bubble-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(10px);
        border-radius: 35px;
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.5);
    }

    /* Giriş Ekranı Logo Konteynırı */
    .logo-container {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    
    /* Buton Tasarımı */
    div.stButton > button {
        background: #ffffff !important;
        color: #1e3c72 !important;
        border-radius: 25px !important;
        height: 4em !important;
        font-weight: 700 !important;
        border: none !important;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1) !important;
    }

    .camera-bubble {
        width: 100%;
        max-width: 750px;
        aspect-ratio: 16/9;
        margin: 0 auto;
        background: #f0f4f8;
        border-radius: 25px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #94a3b8;
        border: 2px solid #e2e8f0;
    }

    header, footer, #MainMenu {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Oturum Durumu
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'active_request' not in st.session_state:
    st.session_state['active_request'] = {"Plaka": "34 BAA 001", "Saat": "05:40:12"}

# --- GİRİŞ EKRANI (LOGO BURADA) ---
if not st.session_state['logged_in']:
    c1, c2, c3 = st.columns([1, 1.2, 1])
    with c2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # LOGO ALANI
        st.markdown("<div class='bubble-card'>", unsafe_allow_html=True)
        if os.path.exists("logo.png"):
            st.image("logo.png", use_container_width=True)
        else:
            st.markdown("<h2 style='text-align:center;'>BULUTO</h2>", unsafe_allow_html=True)
        
        st.markdown("<p style='text-align:center; opacity:0.6;'>Güvenli Yönetim Paneli</p>", unsafe_allow_html=True)
        
        u = st.text_input("Yönetici")
        p = st.text_input("Şifre", type="password")
        
        if st.button("SİSTEME GİRİŞ YAP", use_container_width=True):
            if u == "admin" and p == "buluto2024":
                st.session_state['logged_in'] = True
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- PANEL ---
else:
    # Header
    st.markdown(f"""
    <div style="display: flex; justify-content: space-between; padding: 20px 40px;">
        <div style="font-weight: 800; font-size: 24px; color: white;">BULUTO <span style="font-weight:300;">PRO</span></div>
        <div style="background: rgba(255,255,255,0.3); padding: 8px 25px; border-radius: 30px; color: white;">● SİSTEM AKTİF</div>
    </div>
    """, unsafe_allow_html=True)

    col_l, col_m, col_r = st.columns([1, 3.5, 1])
    
    with col_m:
        # Kamera Balonu
        st.markdown("<div class='bubble-card'>", unsafe_allow_html=True)
        st.markdown("<div class='camera-bubble'>CANLI GÖRÜNTÜ AKTARILIYOR...</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # Plaka ve Karar Balonu
        if st.session_state['active_request']:
            req = st.session_state['active_request']
            st.markdown(f"""
            <div class='bubble-card' style='text-align:center;'>
                <p style='color: #64748b; font-size: 14px;'>TESPİT EDİLEN</p>
                <h1 style='font-weight:800; font-size:52px; margin:0;'>{req['Plaka']}</h1>
                <p style='color: #94a3b8;'>{req['Saat']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<div class='bubble-card'>", unsafe_allow_html=True)
            b_c1, b_c2 = st.columns(2)
            if b_c1.button("✅ ONAYLA", use_container_width=True):
                st.session_state['active_request'] = None
                st.rerun()
            if b_c2.button("❌ REDDET", use_container_width=True):
                st.session_state['active_request'] = None
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

    # Simülasyon
    with st.sidebar:
        st.markdown("### Test")
        t_p = st.text_input("Plaka")
        if st.button("Gönder"):
            st.session_state['active_request'] = {"Plaka": t_p.upper(), "Saat": datetime.now().strftime("%H:%M")}
            st.rerun()