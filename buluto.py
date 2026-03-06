import streamlit as st
import os
from datetime import datetime

# 1. Sayfa Ayarları (Uygulama ismi sadeleşti)
st.set_page_config(page_title="Buluto Security", layout="wide")

# 2. CSS (Sadece senin istediğin o siyah font ve net baloncuklar)
st.markdown("""
    <style>
    /* Google Fonts Import - Fira Code (Okunabilir Monospace) */
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Fira Code', monospace !important;
    }

    /* Arka Plan: image_f95d59.png'daki orijinal mavi */
    .stApp {
        background: linear-gradient(180deg, #4facfe 0%, #00f2fe 100%);
    }
    
    /* NET VE BELİRGİN BEYAZ BALONCUK (Saydam değil, net!) */
    .clear-bubble {
        background-color: rgba(255, 255, 255, 0.95); /* Net beyaz */
        border-radius: 25px;
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
        text-align: center;
        border: 1px solid #e1e8ed;
    }

    /* KAMERA VİZÖRÜ (Kutunun içinde ve net) */
    .vizor-box {
        width: 100%;
        height: 350px;
        background-color: #f1f5f9;
        border-radius: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #64748b;
        font-size: 14px;
        border: 2px solid #e2e8f0;
    }

    /* PLAKA YAZISI - TAM İSTEDİĞİN GİBİ SİYAH VE BELİRGİN */
    .plaka-num {
        font-size: 56px !important;
        font-weight: 700;
        color: #000000 !important; /* KESİNLİKE SİYAH */
        letter-spacing: 5px;
        margin: 15px 0;
    }

    /* 3D BUTONLAR (image_f8f3fd.png - Doğru Renkler) */
    div.stButton > button {
        border-radius: 15px !important;
        font-weight: 700 !important;
        height: 60px !important;
        border: none !important;
        color: white !important;
        transition: all 0.1s !important;
    }

    /* ONAY BUTONU - Turkuaz (Soldaki) */
    .st-emotion-cache-19rxjzo div:nth-child(1) button {
        background: #00bcd4 !important;
        border-bottom: 5px solid #008ba3 !important;
        box-shadow: 0 4px #008ba3 !important;
    }

    /* RED BUTONU - Kırmızı (Sağdaki) */
    .st-emotion-cache-19rxjzo div:nth-child(2) button {
        background: #ff4b5c !important;
        border-bottom: 5px solid #d43d4c !important;
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

# Durum Yönetimi
if 'active_request' not in st.session_state:
    st.session_state['active_request'] = {"Plaka": "34 BAA 001", "Saat": "05:40:12"}

# --- ARAYÜZ ---
st.markdown("<br>", unsafe_allow_html=True)
col_l, col_m, col_r = st.columns([1, 3.5, 1])

with col_m:
    # Başlık
    st.markdown("<h1 style='text-align:center; color:white; font-weight:700;'>BULUTO SECURITY</h1>", unsafe_allow_html=True)
    
    # 1. Baloncuk: Kamera
    st.markdown("<div class='clear-bubble'>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:12px; color:#64748b; margin-bottom:10px;'>LIVE VIDEO FEED</p>", unsafe_allow_html=True)
    st.markdown("<div class='vizor-box'>SİSTEM ANALİZ EDİLİYOR...</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # 2. Baloncuk: Plaka (Yazılar içine girdi ve siyah oldu)
    if st.session_state['active_request']:
        req = st.session_state['active_request']
        st.markdown("<div class='clear-bubble'>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:12px; color:#64748b;'>ALGILANAN PLAKA</p>", unsafe_allow_html=True)
        st.markdown(f"<div class='plaka-num'>{req['Plaka']}</div>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size:11px; color:#94a3b8;'>Giriş Talebi: {req['Saat']}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # 3. 3D Butonlar
        c1, c2 = st.columns(2)
        with c1:
            if st.button("✅ ONAYLA", use_container_width=True):
                st.session_state['active_request'] = None
                st.rerun()
        with c2:
            if st.button("❌ REDDET", use_container_width=True):
                st.session_state['active_request'] = None
                st.rerun()

with st.sidebar:
    st.markdown("### Simülatör")
    t_p = st.text_input("Plaka")
    if st.button("Kameraya Gönder"):
        st.session_state['active_request'] = {"Plaka": t_p.upper(), "Saat": datetime.now().strftime("%H:%M:%S")}
        st.rerun()