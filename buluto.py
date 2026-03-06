import streamlit as st
import os
from datetime import datetime

# 1. Sayfa Konfigürasyonu
st.set_page_config(page_title="Buluto Security Pro", layout="wide")

# 2. CSS (Barlar daraltıldı, Plaka arkası dolduruldu)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@700&family=Lexend:wght@800&display=swap');

    html, body, [class*="css"] { font-family: 'Lexend', sans-serif !important; }

    /* Arka Plan */
    .stApp { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); }
    
    /* KAMERA VİZÖRÜ (Kocaman ve net) */
    .vizor {
        width: 100%;
        height: 380px;
        background-color: #f8fafc;
        border-radius: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #94a3b8;
        border: 2px solid #e2e8f0;
        /* ÜSTTEKİ BAR DARALTILDI */
        margin-top: 5px; 
    }

    /* PLAKA KARTI - ARKASI DOLDURULDU (Koyu Mavi) */
    .main-card.plaka-card {
        background-color: #1e3c72; /* Doldurulan Koyu Mavi */
        border-radius: 20px;
        padding: 20px;
        /* ALTTTAKİ BAR DARALTILDI */
        margin-top: 5px; 
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
        text-align: center;
        color: white; /* Yazı rengi beyaza çekildi */
    }

    /* PLAKA YAZISI - SİYAH/BEYAZ KONTRASTI */
    .plaka-num {
        font-family: 'Fira Code', monospace !important;
        font-size: 52px !important;
        font-weight: 700;
        color: #ffffff !important; /* Doldurulan arka plana göre beyaz yazı */
        letter-spacing: 5px;
        margin: 5px 0;
    }

    /* 3D BUTONLAR (image_f8f3fd.png Stili) */
    div.stButton > button {
        border-radius: 15px !important;
        font-weight: 800 !important;
        height: 60px !important;
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
        border-bottom: 1px solid transparent !important;
        box-shadow: none !important;
    }

    /* Streamlit'in kendi boşluklarını da daraltalım */
    .block-container { padding-top: 1rem !important; padding-bottom: 1rem !important; }
    .stVerticalBlock { gap: 0.5rem !important; }

    header, footer, #MainMenu {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Oturum ve Veri
if 'active_request' not in st.session_state:
    st.session_state['active_request'] = {"Plaka": "34 BAA 001", "Saat": "05:40:12"}

# --- DASHBOARD ---
st.markdown("<h1 style='text-align:center; color:white; font-weight:800; margin-top:20px; font-size:32px;'>BULUTO SECURITY PRO</h1>", unsafe_allow_html=True)

_, main_col, _ = st.columns([1, 3.5, 1])

with main_col:
    # 1. Balon: Kamera (Barlar daraltıldı!)
    st.markdown("<div class='vizor'>CANLI GÖRÜNTÜ YÜKLENİYOR...</div>", unsafe_allow_html=True)

    # 2. Balon: Plaka Bilgisi (Arkası dolduruldu!)
    if st.session_state['active_request']:
        req = st.session_state['active_request']
        st.markdown("<div class='main-card plaka-card'>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:12px; color:#a3b3cc; margin-bottom:0;'>TESPİT EDİLEN PLAKA</p>", unsafe_allow_html=True)
        st.markdown(f"<div class='plaka-num'>{req['Plaka']}</div>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size:11px; color:#a3b3cc; opacity:0.8;'>Giriş Talebi: {req['Saat']}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # 3. 3D Butonlar
        c1, c2 = st.columns(2)
        with c1:
            if st.button("✅ ONAYLA VE AÇ", use_container_width=True):
                st.session_state['active_request'] = None
                st.rerun()
        with c2:
            if st.button("❌ GİRİŞİ ENGELLE", use_container_width=True):
                st.session_state['active_request'] = None
                st.rerun()

# Sidebar (Temiz test alanı)
with st.sidebar:
    if os.path.exists("logo.png"): st.image("logo.png")
    st.markdown("---")
    t_p = st.text_input("Plaka")
    if st.button("Kameraya Gönder"):
        st.session_state['active_request'] = {"Plaka": t_p.upper(), "Saat": datetime.now().strftime("%H:%M:%S")}
        st.rerun()