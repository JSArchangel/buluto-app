import streamlit as st
import os
from datetime import datetime

# 1. Sayfa Ayarları
st.set_page_config(page_title="Buluto Security", layout="wide")

# 2. CSS (Gereksiz tüm boş kutular silindi, sadece plaka ve video kaldı)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@700&family=Lexend:wght@800&display=swap');

    html, body, [class*="css"] { font-family: 'Lexend', sans-serif !important; }

    /* Arka Plan */
    .stApp { background: linear-gradient(180deg, #4facfe 0%, #00f2fe 100%); }
    
    /* ANA KART (Video ve Plaka için) */
    .main-card {
        background-color: white;
        border-radius: 25px;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        text-align: center;
    }

    /* VİDEO ALANI */
    .video-vizor {
        width: 100%;
        height: 380px;
        background-color: #f8fafc;
        border-radius: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #94a3b8;
        border: 2px solid #f1f5f9;
        font-weight: bold;
    }

    /* PLAKA - SİYAH VE FIRA CODE */
    .plaka-box {
        font-family: 'Fira Code', monospace !important;
        font-size: 55px !important;
        font-weight: 700;
        color: #000000 !important;
        letter-spacing: 5px;
        margin: 10px 0;
    }

    /* 3D BUTONLAR */
    div.stButton > button {
        border-radius: 18px !important;
        font-weight: 800 !important;
        height: 65px !important;
        border: none !important;
        color: white !important;
        transition: all 0.1s !important;
    }

    /* ONAYLA - Turkuaz */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {
        background: #00bcd4 !important;
        border-bottom: 6px solid #008ba3 !important;
        box-shadow: 0 4px #008ba3 !important;
    }

    /* REDDET - Kırmızı */
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {
        background: #ff4b5c !important;
        border-bottom: 6px solid #d43d4c !important;
        box-shadow: 0 4px #d43d4c !important;
    }

    div.stButton > button:active {
        transform: translateY(4px) !important;
        border-bottom: 2px solid transparent !important;
    }

    header, footer, #MainMenu {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Oturum
if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False
if 'active_request' not in st.session_state: st.session_state['active_request'] = {"Plaka": "34 BAA 001", "Saat": "05:40:12"}

# --- GİRİŞ EKRANI ---
if not st.session_state['logged_in']:
    _, login_col, _ = st.columns([1, 1.2, 1])
    with login_col:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        if os.path.exists("logo.png"): st.image("logo.png", use_container_width=True)
        st.markdown("<p style='color:#64748b;'>Panel Girişi</p>", unsafe_allow_html=True)
        u = st.text_input("Kullanıcı")
        p = st.text_input("Şifre", type="password")
        if st.button("SİSTEME GİRİŞ YAP"):
            if u == "admin" and p == "buluto2024":
                st.session_state['logged_in'] = True
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- ANA EKRAN ---
else:
    st.markdown("<h1 style='text-align:center; color:white; font-weight:800; margin-top:10px;'>BULUTO SECURITY</h1>", unsafe_allow_html=True)
    
    _, main_col, _ = st.columns([1, 3, 1])
    
    with main_col:
        # 1. KUTU: SADECE VİDEO (Üstteki boş kutu silindi!)
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.markdown("<div class='video-vizor'>CANLI GÖRÜNTÜ AKTARILIYOR...</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # 2. KUTU: PLAKA + YAZI BİRLEŞİK (Alttaki boş kutu silindi!)
        if st.session_state['active_request']:
            req = st.session_state['active_request']
            st.markdown("<div class='main-card'>", unsafe_allow_html=True)
            st.markdown("<p style='font-size:12px; color:#64748b; font-weight:bold; margin:0;'>TESPİT EDİLEN</p>", unsafe_allow_html=True)
            st.markdown(f"<div class='plaka-box'>{req['Plaka']}</div>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size:11px; color:#94a3b8;'>Saat: {req['Saat']}</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            # Butonlar
            b1, b2 = st.columns(2)
            with b1:
                if st.button("✅ ONAYLA", use_container_width=True):
                    st.session_state['active_request'] = None
                    st.rerun()
            with b2:
                if st.button("❌ REDDET", use_container_width=True):
                    st.session_state['active_request'] = None
                    st.rerun()

    # Sidebar Logosu
    with st.sidebar:
        if os.path.exists("logo.png"): st.image("logo.png")
        st.markdown("---")
        t_p = st.text_input("Plaka Simüle Et")
        if st.button("Gönder"):
            st.session_state['active_request'] = {"Plaka": t_p.upper(), "Saat": datetime.now().strftime("%H:%M:%S")}
            st.rerun()