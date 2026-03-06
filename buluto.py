import streamlit as st
import os
from datetime import datetime

# 1. Sayfa Konfigürasyonu
st.set_page_config(page_title="Buluto Security Pro", layout="wide")

# 2. CSS - 3D Derinlik ve Gölge Tasarımı
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@700&family=Lexend:wght@800&display=swap');

    html, body, [class*="css"] { font-family: 'Lexend', sans-serif !important; }

    /* Arka Plan */
    .stApp { background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); }
    
    /* 3D ANA KARTLAR (Tüm kutular artık derinlikli) */
    .main-card {
        background-color: #ffffff;
        border-radius: 30px;
        padding: 30px;
        margin-bottom: 30px;
        /* Figma tarzı çok katmanlı gölge: 1.Yumuşak yayılım, 2.Keskin alt gölge */
        box-shadow: 0 10px 20px rgba(0,0,0,0.1), 
                    0 6px 6px rgba(0,0,0,0.1),
                    inset 0 -8px 0 rgba(0,0,0,0.05); 
        text-align: center;
        border: 1px solid rgba(255,255,255,0.8);
    }

    /* VİDEO VİZÖRÜ - İçbükey (İçe basık) 3D Efekti */
    .video-vizor {
        width: 100%;
        height: 400px;
        background-color: #f1f5f9;
        border-radius: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #94a3b8;
        font-weight: bold;
        /* İç gölge ile derinlik hissi */
        box-shadow: inset 5px 5px 15px rgba(0,0,0,0.05), 
                    inset -5px -5px 15px rgba(255,255,255,0.8);
    }

    /* PLAKA YAZISI - SİYAH VE FIRA CODE */
    .plaka-num {
        font-family: 'Fira Code', monospace !important;
        font-size: 64px !important;
        font-weight: 700;
        color: #000000 !important;
        letter-spacing: 6px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1); /* Yazıda bile hafif derinlik */
    }

    /* 3D BUTONLAR (Figma'daki o basılabilir his) */
    div.stButton > button {
        border-radius: 20px !important;
        font-weight: 800 !important;
        height: 75px !important;
        border: none !important;
        color: white !important;
        font-size: 20px !important;
        transition: all 0.1s ease !important;
    }

    /* ONAYLA - Turkuaz 3D */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {
        background: #00bcd4 !important;
        border-bottom: 8px solid #0097a7 !important; /* Alt kalınlık */
        box-shadow: 0 6px 0 #008ba3, 0 12px 20px rgba(0,0,0,0.2) !important;
    }

    /* REDDET - Kırmızı 3D */
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {
        background: #ff4b5c !important;
        border-bottom: 8px solid #d32f2f !important;
        box-shadow: 0 6px 0 #b71c1c, 0 12px 20px rgba(0,0,0,0.2) !important;
    }

    /* Butona Basılma Hissi */
    div.stButton > button:active {
        transform: translateY(4px) !important;
        border-bottom: 2px solid transparent !important;
        box-shadow: 0 2px 0 rgba(0,0,0,0.2) !important;
    }

    header, footer, #MainMenu {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Durum Yönetimi
if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False
if 'active_request' not in st.session_state: st.session_state['active_request'] = {"Plaka": "34 BAA 001", "Saat": "05:40:12"}

# --- GİRİŞ PANELİ ---
if not st.session_state['logged_in']:
    _, login_col, _ = st.columns([1, 1.3, 1])
    with login_col:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        if os.path.exists("logo.png"): st.image("logo.png", use_container_width=True)
        u = st.text_input("Yönetici")
        p = st.text_input("Şifre", type="password")
        if st.button("SİSTEME GİRİŞ YAP", use_container_width=True):
            if u == "admin" and p == "buluto2024":
                st.session_state['logged_in'] = True
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- ANA DASHBOARD ---
else:
    st.markdown("<h1 style='text-align:center; color:white; font-weight:800; margin-top:20px; text-shadow: 3px 3px 6px rgba(0,0,0,0.2);'>BULUTO SECURITY PRO</h1>", unsafe_allow_html=True)
    
    _, main_col, _ = st.columns([1, 3, 1])
    
    with main_col:
        # 1. Kutu: Video (Derinlikli)
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.markdown("<div class='video-vizor'>CANLI GÖRÜNTÜ AKTARILIYOR...</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # 2. Kutu: Plaka Bilgisi (Tek kart, Siyah yazı)
        if st.session_state['active_request']:
            req = st.session_state['active_request']
            st.markdown("<div class='main-card'>", unsafe_allow_html=True)
            st.markdown("<p style='font-size:14px; color:#64748b; font-weight:bold; margin-bottom:5px;'>ALGILANAN PLAKA</p>", unsafe_allow_html=True)
            st.markdown(f"<div class='plaka-num'>{req['Plaka']}</div>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size:12px; color:#94a3b8;'>Saat: {req['Saat']}</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            # 3D Butonlar
            b1, b2 = st.columns(2)
            with b1:
                if st.button("✅ ONAYLA VE AÇ", use_container_width=True):
                    st.session_state['active_request'] = None
                    st.rerun()
            with b2:
                if st.button("❌ GİRİŞİ ENGELLE", use_container_width=True):
                    st.session_state['active_request'] = None
                    st.rerun()