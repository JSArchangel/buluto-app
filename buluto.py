import streamlit as st
import os
from datetime import datetime

# 1. Sayfa Ayarları
st.set_page_config(page_title="Buluto Security Pro", layout="wide")

# 2. CSS - Sadece Plaka Hizalaması Düzeltildi, Diğer Her Şey Aynı
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@700&family=Lexend:wght@800&display=swap');

    html, body, [class*="css"] { font-family: 'Lexend', sans-serif !important; }

    .stApp { 
        background: linear-gradient(180deg, #00c6ff 0%, #0072ff 100%); 
    }
    
    .glass-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 25px;
        padding: 20px;
        margin-bottom: 25px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2), inset 0 -5px 0 rgba(0, 0, 0, 0.1);
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }

    .video-container {
        width: 100%;
        height: 380px;
        background-color: #1e293b;
        border-radius: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #38bdf8;
        font-weight: bold;
        box-shadow: inset 0 0 50px rgba(0,0,0,0.5);
        border: 4px solid #f8fafc;
    }

    /* PLAKA KARTI - ORTALAMA DÜZELTİLDİ */
    .plaka-bg {
        background: #0f172a; 
        border-radius: 20px;
        padding: 25px;
        margin: 15px auto;
        box-shadow: 0 10px 0 #000;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* PLAKA METNİ - NEON VE SİMETRİK */
    .plaka-num {
        font-family: 'Fira Code', monospace !important;
        font-size: 58px !important;
        font-weight: 700;
        color: #ffffff !important;
        letter-spacing: 8px; 
        padding-left: 8px; /* Sağdaki harf boşluğunu dengelemek için kritik! */
        text-shadow: 0 0 1px #fff, 0 0 3px #38bdf8, 0 0 30px #38bdf8, 0 0 40px #38bdf8;
        text-align: center;
    }

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

    # --- GİRİŞ EKRANI (LOGOLU) ---
if not st.session_state['logged_in']:
    _, login_col, _ = st.columns([1, 1.2, 1])
    with login_col:
        # Üstteki gereksiz boşlukları ve barı önlemek için sadece küçük bir mesafe:
        st.write("") 
        
        # Kartın başlangıcı
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        
        # Logoyu direkt en üste alıyoruz
        if os.path.exists("logo.png"): 
            st.image("logo.png", use_container_width=True)
        
        u = st.text_input("Yönetici")
        p = st.text_input("Şifre", type="password")
        
        if st.button("GİRİŞ YAP", use_container_width=True):
            if u == "admin" and p == "buluto2024":
                st.session_state['logged_in'] = True
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {
        background: #ff4b5c !important;
        border-bottom: 8px solid #cc3344 !important;
    }

    div.stButton > button:active { transform: translateY(6px) !important; }

    header, footer, #MainMenu {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Oturum Durumu
if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False
if 'active_request' not in st.session_state: st.session_state['active_request'] = {"Plaka": "34 BAA 001", "Saat": "05:40:12"}

# --- GİRİŞ EKRANI (LOGOLU) ---
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

# --- ANA DASHBOARD ---
else:
    st.markdown("<h1 style='text-align:center; color:white; font-weight:900;'>BULUTO SECURITY PRO</h1>", unsafe_allow_html=True)
    
    _, main_col, _ = st.columns([1, 3.2, 1])
    
    with main_col:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<div class='label-tag'>CANLI KAMERA AKIŞI</div>", unsafe_allow_html=True)
        st.markdown("<div class='video-container'>SİSTEM ANALİZ EDİLİYOR...</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        if st.session_state['active_request']:
            req = st.session_state['active_request']
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            st.markdown("<div class='label-tag'>TESPİT EDİLEN ARAÇ</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='plaka-bg'><div class='plaka-num'>{req['Plaka']}</div></div>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:#64748b; font-weight:bold;'>Talep Saati: {req['Saat']}</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            b1, b2 = st.columns(2)
            with b1:
                if st.button("✅ ONAYLA VE AÇ", use_container_width=True):
                    st.session_state['active_request'] = None
                    st.rerun()
            with b2:
                if st.button("❌ GİRİŞİ ENGELLE", use_container_width=True):
                    st.session_state['active_request'] = None
                    st.rerun()

    # Sidebar Simülasyonu (Logo Dahil)
    with st.sidebar:
        if os.path.exists("logo.png"): st.image("logo.png")
        st.markdown("---")
        t_p = st.text_input("Plaka Simüle Et")
        if st.button("Kameraya Gönder"):
            st.session_state['active_request'] = {"Plaka": t_p.upper(), "Saat": datetime.now().strftime("%H:%M:%S")}
            st.rerun()