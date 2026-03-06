import streamlit as st
import os
from datetime import datetime

# 1. Sayfa Konfigürasyonu
st.set_page_config(page_title="Buluto Security", layout="wide")

# 2. CSS - (Saydam Cam Baloncuklar ve Görseldeki 3D Butonlar)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@400;800&display=swap');
    html, body, [class*="css"] { font-family: 'Lexend', sans-serif !important; }

    /* Arka Plan: Orijinal Mavi */
    .stApp { background: linear-gradient(180deg, #4facfe 0%, #00f2fe 100%); }
    
    /* GERÇEK SAYDAM BALONCUK (image_f8f07d.png gibi) */
    .glass-bubble {
        background: rgba(255, 255, 255, 0.22);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 2px solid rgba(255, 255, 255, 0.4);
        border-radius: 30px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        text-align: center;
        color: white;
    }

    /* Kamera Alanı */
    .camera-vizor {
        width: 100%;
        height: 350px;
        background: rgba(0, 0, 0, 0.1);
        border-radius: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    /* Plaka Fontu (Kameradan Küçük) */
    .plaka-style {
        font-size: 38px !important;
        font-weight: 800;
        letter-spacing: 5px;
        margin: 5px 0;
    }

    /* 3D BUTONLAR - image_f8f3fd.png Stili */
    div.stButton > button {
        border-radius: 15px !important;
        font-weight: 800 !important;
        height: 60px !important;
        border: none !important;
        color: white !important;
        transition: all 0.1s !important;
    }

    /* SOL BUTON: ONAYLA (Turkuaz 3D) */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {
        background: #00bcd4 !important;
        border-bottom: 6px solid #008ba3 !important;
        box-shadow: 0 4px #008ba3 !important;
    }

    /* SAĞ BUTON: REDDET (Kırmızı 3D) */
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

if 'active_request' not in st.session_state:
    st.session_state['active_request'] = {"Plaka": "34 BAA 001", "Saat": "05:40:12"}

# --- DASHBOARD ---
st.markdown("<br>", unsafe_allow_html=True)
c_l, c_main, c_r = st.columns([1, 3, 1])

with c_main:
    st.markdown("<h1 style='text-align:center; color:white; font-weight:800; margin-bottom:20px;'>BULUTO SECURITY</h1>", unsafe_allow_html=True)
    
    # Kamera Baloncuğu
    st.markdown("<div class='glass-bubble'>", unsafe_allow_html=True)
    st.markdown("<div class='camera-vizor'>CANLI GÖRÜNTÜ YÜKLENİYOR...</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Plaka Baloncuğu
    if st.session_state['active_request']:
        req = st.session_state['active_request']
        st.markdown("<div class='glass-bubble'>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:12px; opacity:0.8;'>ALGILANAN ARAÇ</p>", unsafe_allow_html=True)
        st.markdown(f"<div class='plaka-style'>{req['Plaka']}</div>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size:11px; opacity:0.6;'>Saat: {req['Saat']}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # 3D Butonlar
        b1, b2 = st.columns(2)
        with b1:
            if st.button("✅ ONAYLA", use_container_width=True):
                st.session_state['active_request'] = None
                st.rerun()
        with b2:
            if st.button("❌ REDDET", use_container_width=True):
                st.session_state['active_request'] = None
                st.rerun()

with st.sidebar:
    st.markdown("### Test Paneli")
    t_p = st.text_input("Plaka")
    if st.button("Gönder"):
        st.session_state['active_request'] = {"Plaka": t_p.upper(), "Saat": datetime.now().strftime("%H:%M")}
        st.rerun()