import streamlit as st
import os
from datetime import datetime

# 1. Sayfa Ayarı
st.set_page_config(page_title="Buluto Security", layout="wide")

# 2. CSS - (Gerçek Glassmorphism ve 3D Butonlar)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@400;800&display=swap');
    html, body, [class*="css"] { font-family: 'Lexend', sans-serif !important; }

    /* Arka Plan: İstediğin Orijinal Mavi Gradyan */
    .stApp { background: linear-gradient(180deg, #4facfe 0%, #00f2fe 100%); }
    
    /* GERÇEK CAM BALONCUK (image_f8f07d.png'deki gibi) */
    .glass-card {
        background: rgba(255, 255, 255, 0.2); 
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 2px solid rgba(255, 255, 255, 0.3);
        border-radius: 35px;
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
        text-align: center;
        color: white;
    }

    /* KAMERA VİZÖRÜ (Kutunun içinde, orantılı) */
    .vizor {
        width: 100%;
        height: 320px;
        background: rgba(0, 0, 0, 0.15);
        border-radius: 25px;
        display: flex;
        justify-content: center;
        align-items: center;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    /* PLAKA (Kameradan küçük, çok net) */
    .plaka-num {
        font-size: 42px !important;
        font-weight: 800;
        letter-spacing: 6px;
        margin: 10px 0;
        color: white;
    }

    /* 3D BUTONLAR (image_f8f3fd.png - Tam Renkler) */
    div.stButton > button {
        border-radius: 18px !important;
        font-weight: 800 !important;
        height: 65px !important;
        border: none !important;
        color: white !important;
        transition: transform 0.1s, box-shadow 0.1s !important;
    }

    /* ONAY BUTONU: Turkuaz 3D */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {
        background: #00bcd4 !important;
        border-bottom: 6px solid #008ba3 !important;
        box-shadow: 0 4px #008ba3 !important;
    }

    /* RED BUTONU: Kırmızı/Mercan 3D */
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {
        background: #ff4b5c !important;
        border-bottom: 6px solid #d43d4c !important;
        box-shadow: 0 4px #d43d4c !important;
    }

    /* Basılma Efekti */
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

# --- ARAYÜZ ---
st.markdown("<br>", unsafe_allow_html=True)
_, main_col, _ = st.columns([1, 3.5, 1])

with main_col:
    # Başlık
    st.markdown("<h1 style='text-align:center; color:white; font-weight:800; letter-spacing:-1px;'>BULUTO SECURITY</h1>", unsafe_allow_html=True)
    
    # 1. Balon: Kamera
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:11px; opacity:0.7; margin-bottom:10px;'>LIVE VIDEO FEED</p>", unsafe_allow_html=True)
    st.markdown("<div class='vizor'>SİSTEM ANALİZ EDİLİYOR...</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # 2. Balon: Plaka Bilgisi
    if st.session_state['active_request']:
        req = st.session_state['active_request']
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:11px; opacity:0.7;'>TESPİT EDİLEN PLAKA</p>", unsafe_allow_html=True)
        st.markdown(f"<div class='plaka-num'>{req['Plaka']}</div>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size:11px; opacity:0.5;'>Giriş Talebi: {req['Saat']}</p>", unsafe_allow_html=True)
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
    new_p = st.text_input("Plaka")
    if st.button("Gönder"):
        st.session_state['active_request'] = {"Plaka": new_p.upper(), "Saat": datetime.now().strftime("%H:%M:%S")}
        st.rerun()