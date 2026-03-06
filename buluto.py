import streamlit as st
import os
from datetime import datetime

# 1. Sayfa Ayarları
st.set_page_config(page_title="Buluto Security Pro", layout="wide")

# 2. CSS - 3D Derinlik, Dolu Arka Planlar ve Net Katmanlar
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@700&family=Lexend:wght@800&display=swap');

    html, body, [class*="css"] { font-family: 'Lexend', sans-serif !important; }

    /* Arka Plan: Daha profesyonel bir geçiş */
    .stApp { 
        background: linear-gradient(180deg, #00c6ff 0%, #0072ff 100%); 
    }
    
    /* GENEL KUTU YAPISI (Arka Planı Dolu ve 3D) */
    .glass-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 25px;
        padding: 20px;
        margin-bottom: 25px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2), 
                    inset 0 -5px 0 rgba(0, 0, 0, 0.1);
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }

    /* KAMERA ALANI */
    .video-container {
        width: 100%;
        height: 380px;
        background-color: #1e293b; /* Koyu dolgu */
        border-radius: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #38bdf8;
        font-weight: bold;
        box-shadow: inset 0 0 50px rgba(0,0,0,0.5);
        border: 4px solid #f8fafc;
    }

    /* PLAKA KARTINI TAMAMEN DOLDURUYORUZ (Koyu Lacivert/Siyah Arka Plan) */
    .plaka-bg {
        background: #0f172a; 
        border-radius: 20px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 10px 0 #000; /* 3D alt taban */
    }

    /* PLAKA METNİ - KESKİN VE NET */
    .plaka-num {
        font-family: 'Fira Code', monospace !important;
        font-size: 58px !important;
        font-weight: 700;
        color: #ffffff !important;
        letter-spacing: 8px;
        text-shadow: 0 0 15px rgba(56, 189, 248, 0.5);
    }

    /* ETİKETLER (Yazıların karışmaması için ayrı kutu) */
    .label-tag {
        background: #38bdf8;
        color: #0f172a;
        padding: 5px 15px;
        border-radius: 10px;
        font-size: 12px;
        display: inline-block;
        margin-bottom: 10px;
        font-weight: bold;
    }

    /* 3D BUTONLAR (Figma Stili) */
    div.stButton > button {
        border-radius: 20px !important;
        font-weight: 800 !important;
        height: 70px !important;
        border: none !important;
        color: white !important;
        font-size: 18px !important;
        transition: transform 0.1s !important;
    }

    /* ONAYLA - Turkuaz 3D */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {
        background: #00d2ff !important;
        border-bottom: 8px solid #0099cc !important;
        box-shadow: 0 10px 20px rgba(0, 210, 255, 0.3) !important;
    }

    /* REDDET - Kırmızı 3D */
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {
        background: #ff4b5c !important;
        border-bottom: 8px solid #cc3344 !important;
        box-shadow: 0 10px 20px rgba(255, 75, 92, 0.3) !important;
    }

    div.stButton > button:active {
        transform: translateY(6px) !important;
        border-bottom: 2px solid transparent !important;
    }

    header, footer, #MainMenu {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Oturum Durumu
if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False
if 'active_request' not in st.session_state: st.session_state['active_request'] = {"Plaka": "34 BAA 001", "Saat": "05:40:12"}

# --- GİRİŞ PANELİ ---
if not st.session_state['logged_in']:
    _, login_col, _ = st.columns([1, 1.2, 1])
    with login_col:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        if os.path.exists("logo.png"): st.image("logo.png", use_container_width=True)
        u = st.text_input("Yönetici")
        p = st.text_input("Şifre", type="password")
        if st.button("GİRİŞ YAP", use_container_width=True):
            if u == "admin" and p == "buluto2024":
                st.session_state['logged_in'] = True
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- ANA EKRAN ---
else:
    st.markdown("<h1 style='text-align:center; color:white; font-weight:900; letter-spacing:2px;'>BULUTO SECURITY <span style='color:#0f172a'>PRO</span></h1>", unsafe_allow_html=True)
    
    _, main_col, _ = st.columns([1, 3.2, 1])
    
    with main_col:
        # 1. Video Bloğu
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<div class='label-tag'>CANLI KAMERA AKIŞI</div>", unsafe_allow_html=True)
        st.markdown("<div class='video-container'>SİSTEM ANALİZ EDİLİYOR...</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # 2. Plaka Bloğu (Dolu Arka Plan)
        if st.session_state['active_request']:
            req = st.session_state['active_request']
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            st.markdown("<div class='label-tag'>TESPİT EDİLEN ARAÇ</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='plaka-bg'><div class='plaka-num'>{req['Plaka']}</div></div>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:#64748b; font-weight:bold;'>Talebi Saati: {req['Saat']}</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            # 3. Aksiyon Butonları
            b1, b2 = st.columns(2)
            with b1:
                if st.button("✅ ONAYLA VE AÇ", use_container_width=True):
                    st.session_state['active_request'] = None
                    st.rerun()
            with b2:
                if st.button("❌ GİRİŞİ ENGELLE", use_container_width=True):
                    st.session_state['active_request'] = None
                    st.rerun()