import streamlit as st
import os
from datetime import datetime
import time

# 1. Sayfa Konfigürasyonu
st.set_page_config(
    page_title="Buluto Security Pro",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS MASTER - Beyaz barı ve boşlukları kökten yok eden, tasarımı en tepeye çeken blok
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@700&family=Lexend:wght@800&display=swap');

    /* Sayfa Geneli ve Arkaplan */
    html, body, [class*="css"] { 
        font-family: 'Lexend', sans-serif !important; 
    }
    
    .stApp { 
        background: linear-gradient(180deg, #00c6ff 0%, #0072ff 100%); 
    }

    /* BEYAZ BARI VE GEREKSİZ TÜM ÜST BOŞLUKLARI ÖLDÜREN KISIM */
    [data-testid="stHeader"] {
        display: none !important;
    }
    
    header {
        visibility: hidden !important;
        height: 0px !important;
    }

    .main .block-container {
        padding-top: 0px !important;
        padding-bottom: 0px !important;
        margin-top: -50px !important; /* Bu kısım beyaz boşluğu yukarı çeker */
    }

    #MainMenu { visibility: hidden !important; }
    footer { visibility: hidden !important; }

    /* Glassmorphism Kartları */
    .glass-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 25px;
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }

    /* Video Vizörü */
    .video-container {
        width: 100%;
        height: 400px;
        background-color: #0f172a;
        border-radius: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #38bdf8;
        font-weight: bold;
        border: 4px solid #f8fafc;
        box-shadow: inset 0 0 50px rgba(0,0,0,0.8);
    }

    /* Plaka Tasarımı */
    .plaka-bg {
        background: #0f172a; 
        border-radius: 20px;
        padding: 25px;
        margin: 20px auto;
        box-shadow: 0 10px 0 #000;
        display: flex;
        justify-content: center;
    }
    .plaka-num {
        font-family: 'Fira Code', monospace !important;
        font-size: 64px !important;
        font-weight: 700;
        color: #ffffff !important;
        letter-spacing: 10px;
        padding-left: 10px;
        text-shadow: 0 0 5px #fff, 0 0 15px #38bdf8;
    }

    /* 3D Butonlar */
    div.stButton > button {
        border-radius: 22px !important;
        font-weight: 800 !important;
        height: 75px !important;
        border: none !important;
        color: white !important;
        font-size: 20px !important;
        transition: 0.1s;
    }
    
    /* Giriş Butonu ve Onay Butonu Rengi (Kırmızımsı/Mercan) */
    div.stButton > button {
        background: #ff5555 !important;
        border-bottom: 8px solid #cc4444 !important;
    }
    
    div.stButton > button:active { 
        transform: translateY(6px) !important; 
        border-bottom: 2px solid transparent !important; 
    }

    /* Label Etiketleri */
    .label-tag {
        background: #38bdf8;
        color: #0f172a;
        padding: 6px 18px;
        border-radius: 12px;
        font-size: 13px;
        display: inline-block;
        margin-bottom: 12px;
        font-weight: 800;
    }

    /* Input Alanları Karartma */
    .stTextInput input {
        background-color: #262730 !important;
        color: white !important;
        border-radius: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Session State
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'active_request' not in st.session_state:
    st.session_state['active_request'] = {"Plaka": "34 BAA 001", "Saat": "05:40:12"}
if 'history' not in st.session_state:
    st.session_state['history'] = []

# --- GİRİŞ EKRANI MANTIĞI ---
if not st.session_state['logged_in']:
    _, login_col, _ = st.columns([1, 1.2, 1])
    with login_col:
        st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)
        
        # Logo Kontrolü ve Gösterimi
        if os.path.exists("logo.png"):
            st.image("logo.png", use_container_width=True)
        
        st.markdown("### Yönetici Girişi")
        user = st.text_input("Kullanıcı Adı", key="login_user")
        pw = st.text_input("Şifre", type="password", key="login_pw")
        
        if st.button("SİSTEMİ BAŞLAT", use_container_width=True):
            if user == "admin" and pw == "buluto2024":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("Hatalı Kimlik Bilgileri!")

# --- ANA DASHBOARD MANTIĞI ---
else:
    st.markdown("<h1 style='text-align:center; color:white; font-weight:900; margin-top:20px;'>BULUTO SECURITY PRO</h1>", unsafe_allow_html=True)
    
    with st.sidebar:
        if os.path.exists("logo.png"):
            st.image("logo.png")
        st.markdown("---")
        st.subheader("🛠️ Simülasyon Araçları")
        sim_plaka = st.text_input("Manuel Plaka Girişi")
        if st.button("Kameraya Gönder"):
            if sim_plaka:
                st.session_state['active_request'] = {
                    "Plaka": sim_plaka.upper(),
                    "Saat": datetime.now().strftime("%H:%M:%S")
                }
                st.rerun()
        
        st.markdown("---")
        st.subheader("📜 Son Geçişler")
        for item in st.session_state['history'][-5:]:
            st.write(f"🕒 {item['Saat']} - {item['Plaka']}")
            
        if st.button("Güvenli Çıkış"):
            st.session_state['logged_in'] = False
            st.rerun()

    _, main_col, _ = st.columns([1, 3.5, 1])
    with main_col:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<div class='label-tag'>CANLI KAMERA</div>", unsafe_allow_html=True)
        st.markdown("<div class='video-container'>GÖRÜNTÜ ANALİZ EDİLİYOR...</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        if st.session_state['active_request']:
            req = st.session_state['active_request']
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            st.markdown("<div class='label-tag'>TESPİT EDİLEN ARAÇ</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='plaka-bg'><div class='plaka-num'>{req['Plaka']}</div></div>", unsafe_allow_html=True)
            st.write(f"**Talep Zamanı:** {req['Saat']}")
            st.markdown("</div>", unsafe_allow_html=True)

            b1, b2 = st.columns(2)
            with b1:
                if st.button("✅ GİRİŞE İZİN VER", use_container_width=True):
                    st.session_state['history'].append(req)
                    st.session_state['active_request'] = None
                    st.rerun()
            with b2:
                if st.button("❌ GİRİŞİ ENGELLE", use_container_width=True):
                    st.session_state['active_request'] = None
                    st.rerun()