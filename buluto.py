import streamlit as st
import os
from datetime import datetime

# 1. Sayfa Konfigürasyonu
st.set_page_config(page_title="Buluto Security", layout="wide")

# 2. CSS (Sadece saydam cam baloncuklar ve doğru renkli 3D butonlar)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@400;800&display=swap');

    html, body, [class*="css"] { font-family: 'Lexend', sans-serif !important; }

    /* ARKA PLAN: Orijinal Mavi Gradyan */
    .stApp { background: linear-gradient(180deg, #4facfe 0%, #00f2fe 100%); }
    
    /* GERÇEK CAM BALONCUK (image_f8f07d.png'deki gibi saydam) */
    .glass-bubble {
        background: rgba(255, 255, 255, 0.2); /* Arkasını gösterir */
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 2px solid rgba(255, 255, 255, 0.4); /* Parlayan kenarlar */
        border-radius: 30px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        text-align: center;
        color: white;
    }

    /* KAMERA VİZÖRÜ */
    .camera-area {
        width: 100%;
        height: 350px;
        background: rgba(0, 0, 0, 0.1);
        border-radius: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    /* PLAKA YAZISI (Baloncuk içinde ve dengeli) */
    .plaka-font {
        font-size: 40px !important;
        font-weight: 800;
        letter-spacing: 5px;
        margin: 5px 0;
    }

    /* 3D BUTONLAR (image_f8f3fd.png - Doğru Renkler) */
    div.stButton > button {
        border-radius: 15px !important;
        font-weight: 800 !important;
        height: 60px !important;
        border: none !important;
        transition: all 0.1s !important;
    }

    /* ONAY BUTONU - Turkuaz (Soldaki) */
    .st-emotion-cache-19rxjzo div:nth-child(1) button {
        background: #00bcd4 !important;
        border-bottom: 5px solid #008ba3 !important;
        box-shadow: 0 4px #008ba3 !important;
        color: white !important;
    }

    /* RED BUTONU - Kırmızı (Sağdaki) */
    .st-emotion-cache-19rxjzo div:nth-child(2) button {
        background: #ff4b5c !important;
        border-bottom: 5px solid #d43d4c !important;
        box-shadow: 0 4px #d43d4c !important;
        color: white !important;
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

# --- DASHBOARD ---
st.markdown("<br>", unsafe_allow_html=True)
col_l, col_m, col_r = st.columns([1, 3, 1])

with col_m:
    # Başlık (Sadeleşti)
    st.markdown("<h1 style='text-align:center; color:white; font-weight:800;'>BULUTO SECURITY</h1>", unsafe_allow_html=True)
    
    # Kamera Baloncuğu
    st.markdown("<div class='glass-bubble'>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:12px; opacity:0.8;'>CANLI KAMERA AKIŞI</p>", unsafe_allow_html=True)
    st.markdown("<div class='camera-area'>GÖRÜNTÜ YÜKLENİYOR...</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Plaka Baloncuğu (Yazılar içine girdi)
    if st.session_state['active_request']:
        req = st.session_state['active_request']
        st.markdown("<div class='glass-bubble'>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:12px; opacity:0.8; margin-bottom:0;'>ALGILANAN PLAKA</p>", unsafe_allow_html=True)
        st.markdown(f"<div class='plaka-font'>{req['Plaka']}</div>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size:12px; opacity:0.6;'>Tespit Zamanı: {req['Saat']}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # Karar Butonları (Renkler Düzeldi)
        c1, c2 = st.columns(2)
        with c1:
            if st.button("✅ ONAYLA", use_container_width=True):
                st.session_state['active_request'] = None
                st.rerun()
        with c2:
            if st.button("❌ REDDET", use_container_width=True):
                st.session_state['active_request'] = None
                st.rerun()

# Sidebar (Temiz Test Alanı)
with st.sidebar:
    if os.path.exists("logo.png"): st.image("logo.png")
    t_p = st.text_input("Simülasyon Plakası")
    if st.button("Aracı Gönder"):
        st.session_state['active_request'] = {"Plaka": t_p.upper(), "Saat": datetime.now().strftime("%H:%M")}
        st.rerun()