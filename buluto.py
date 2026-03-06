import streamlit as st
import pandas as pd
from datetime import datetime
import os

# 1. Sayfa Konfigürasyonu
st.set_page_config(page_title="Buluto Pro | Soft UI", layout="wide")

# 2. ÖZEL BALON TEMA (Modern Soft UI & Lexend Font)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;600;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Lexend', sans-serif !important;
    }

    /* Arka Plan: Daha ferah ve iç açıcı geçiş */
    .stApp {
        background: linear-gradient(135deg, #00d2ff 0%, #3a7bd5 100%);
        color: #1e3c72;
    }
    
    /* Balon Kart Yapısı */
    .bubble-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(10px);
        border-radius: 35px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.5);
        transition: all 0.3s ease;
    }
    
    .bubble-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 45px rgba(0, 0, 0, 0.2);
    }

    /* Kamera Vizörü Balonu */
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
        font-weight: 600;
        border: 2px solid #e2e8f0;
    }

    /* Plaka Balonu */
    .plaka-bubble {
        font-size: 52px;
        font-weight: 800;
        color: #1e3c72;
        letter-spacing: 4px;
        margin: 10px 0;
    }

    /* Butonları Gerçek Balon Tuş Yap */
    div.stButton > button {
        background: #ffffff !important;
        color: #1e3c72 !important;
        border-radius: 25px !important;
        height: 4.5em !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        border: none !important;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1) !important;
        transition: all 0.2s ease !important;
        text-transform: uppercase;
    }
    
    div.stButton > button:active {
        transform: scale(0.95) !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1) !important;
    }

    /* Onay ve Red Renkleri */
    .st-emotion-cache-12w0qpk e1nzilvr4 { /* Bu Streamlit'in buton konteynerıdır */
        gap: 20px;
    }

    header, footer, #MainMenu {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Oturum Durumu
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'active_request' not in st.session_state:
    st.session_state['active_request'] = {"Plaka": "34 BAA 001", "Saat": "05:40:12"}

# --- GİRİŞ ---
if not st.session_state['logged_in']:
    c1, c2, c3 = st.columns([1, 1.2, 1])
    with c2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("<div class='bubble-card'><h2 style='text-align:center;'>Buluto Giriş</h2>", unsafe_allow_html=True)
        u = st.text_input("Kullanıcı")
        p = st.text_input("Şifre", type="password")
        if st.button("SİSTEME GİRİŞ", use_container_width=True):
            if u == "admin" and p == "buluto2024":
                st.session_state['logged_in'] = True
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- PANEL ---
else:
    # Header Balonu
    st.markdown(f"""
    <div style="display: flex; justify-content: space-between; padding: 20px 40px;">
        <div style="font-weight: 800; font-size: 24px; color: white; text-shadow: 0 2px 10px rgba(0,0,0,0.2);">BULUTO <span style="font-weight:300;">PRO</span></div>
        <div style="background: rgba(255,255,255,0.3); padding: 8px 25px; border-radius: 30px; color: white; font-weight: 600; backdrop-filter: blur(5px);">
            ● CANLI YAYIN
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_l, col_m, col_r = st.columns([1, 3.5, 1])
    
    with col_m:
        # 1. Balon: Kamera
        st.markdown("<div class='bubble-card'>", unsafe_allow_html=True)
        st.markdown("<div class='camera-bubble'>CANLI GÖRÜNTÜ AKTARILIYOR...</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # 2. Balon: Plaka Bilgisi
        if st.session_state['active_request']:
            req = st.session_state['active_request']
            st.markdown(f"""
            <div class='bubble-card' style='text-align:center;'>
                <p style='color: #64748b; font-size: 14px; letter-spacing: 2px; text-transform: uppercase;'>Tespit Edilen Araç</p>
                <div class='plaka-bubble'>{req['Plaka']}</div>
                <p style='color: #94a3b8;'>Talep Saati: {req['Saat']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # 3. Balon: Karar Butonları
            st.markdown("<div class='bubble-card' style='padding: 20px;'>", unsafe_allow_html=True)
            b_c1, b_c2 = st.columns(2)
            
            with b_c1:
                if st.button("✅ GİRİŞE İZİN VER", use_container_width=True):
                    st.success("KAPI AÇILDI")
                    st.session_state['active_request'] = None
            
            with b_c2:
                if st.button("❌ GİRİŞİ REDDET", use_container_width=True):
                    st.error("REDDEDİLDİ")
                    st.session_state['active_request'] = None
            st.markdown("</div>", unsafe_allow_html=True)

    # Simülasyon (Sidebar)
    with st.sidebar:
        st.markdown("### Test Paneli")
        t_p = st.text_input("Plaka")
        if st.button("Kamera Tetikle"):
            st.session_state['active_request'] = {"Plaka": t_p.upper(), "Saat": datetime.now().strftime("%H:%M:%S")}
            st.rerun()