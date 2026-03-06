import streamlit as st
import os
from datetime import datetime

# 1. Sayfa Konfigürasyonu
st.set_page_config(page_title="Buluto Pro", layout="wide")

# 2. CSS (Hatalardan arındırılmış, 3D buton ve Cam baloncuk odaklı)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@400;800&display=swap');

    html, body, [class*="css"] { font-family: 'Lexend', sans-serif !important; }

    /* ARKA PLAN: image_f95d59.png'daki orijinal mavi */
    .stApp { background: linear-gradient(180deg, #4facfe 0%, #00f2fe 100%); }
    
    /* CAM BALONCUK (Sadece gerekli yerlerde) */
    .glass-bubble {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 2px solid rgba(255, 255, 255, 0.4);
        border-radius: 30px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        text-align: center;
    }

    /* KAMERA VİZÖRÜ (Kocaman ve net) */
    .camera-vizor {
        width: 100%;
        height: 380px;
        background: rgba(0, 0, 0, 0.15);
        border-radius: 20px;
        border: 2px solid rgba(255, 255, 255, 0.3);
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        margin-bottom: 10px;
    }

    /* PLAKA (Kameradan daha ufak ve şık) */
    .plaka-box {
        font-size: 38px !important;
        font-weight: 800;
        color: white;
        letter-spacing: 5px;
        margin: 10px 0;
    }

    /* 3D BUTONLAR (image_f8f3fd.png mantığıyla) */
    div.stButton > button {
        border-radius: 15px !important;
        font-weight: 800 !important;
        height: 55px !important;
        transition: all 0.1s !important;
        border: none !important;
        text-transform: uppercase;
    }

    /* Onay Butonu - Turkuaz */
    div.stButton > button[kind="primary"], .st-emotion-cache-19rxjzo div:nth-child(1) button {
        background: #00bcd4 !important;
        border-bottom: 5px solid #008ba3 !important;
        box-shadow: 0 4px #008ba3 !important;
    }

    /* Red Butonu - Kırmızı */
    div.stButton > button[kind="secondary"], .st-emotion-cache-19rxjzo div:nth-child(2) button {
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

# Oturum Yönetimi
if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False
if 'active_request' not in st.session_state: st.session_state['active_request'] = {"Plaka": "34 BAA 001", "Saat": "05:40:12"}

# --- GİRİŞ EKRANI ---
if not st.session_state['logged_in']:
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("<div class='glass-bubble'>", unsafe_allow_html=True)
        if os.path.exists("logo.png"):
            st.image("logo.png", use_container_width=True)
        st.markdown("<p style='color:white; opacity:0.8;'>Güvenli Yönetim Paneli</p>", unsafe_allow_html=True)
        u = st.text_input("Yönetici")
        p = st.text_input("Şifre", type="password")
        if st.button("SİSTEME GİRİŞ YAP", use_container_width=True):
            if u == "admin" and p == "buluto2024":
                st.session_state['logged_in'] = True
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- ANA DASHBOARD ---
else:
    st.markdown("<h2 style='text-align:center; color:white; font-weight:800; margin-top:20px;'>BULUTO PRO</h2>", unsafe_allow_html=True)
    
    col_l, col_m, col_r = st.columns([1, 4, 1])
    
    with col_m:
        # Kamera Alanı
        st.markdown("<div class='glass-bubble'>", unsafe_allow_html=True)
        st.markdown("<div class='camera-vizor'>CANLI GÖRÜNTÜ AKTARILIYOR...</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # Plaka ve Buton Alanı
        if st.session_state['active_request']:
            req = st.session_state['active_request']
            st.markdown("<div class='glass-bubble'>", unsafe_allow_html=True)
            st.markdown(f"<div class='plaka-box'>{req['Plaka']}</div>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:white; opacity:0.7;'>Tespit: {req['Saat']}</p>", unsafe_allow_html=True)
            
            # Karar Butonları
            b1, b2 = st.columns(2)
            with b1:
                if st.button("✅ ONAYLA", use_container_width=True):
                    st.session_state['active_request'] = None
                    st.rerun()
            with b2:
                if st.button("❌ REDDET", use_container_width=True):
                    st.session_state['active_request'] = None
                    st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

# Sidebar (Temiz ve kodsuz)
with st.sidebar:
    if os.path.exists("logo.png"): st.image("logo.png")
    st.markdown("---")
    t_p = st.text_input("Plaka Simüle Et")
    if st.button("Kameraya Gönder"):
        st.session_state['active_request'] = {"Plaka": t_p.upper(), "Saat": datetime.now().strftime("%H:%M")}
        st.rerun()