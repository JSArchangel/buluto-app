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

# 2. CSS MASTER - Beyaz barı ve boşlukları yok eden, tasarımı koruyan blok
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@700&family=Lexend:wght@800&display=swap');

    /* Sayfa Geneli */
    html, body, [class*="css"] { font-family: 'Lexend', sans-serif !important; }
    .stApp { 
        background: linear-gradient(180deg, #00c6ff 0%, #0072ff 100%); 
    }

    /* BEYAZ BARI VE GEREKSİZ TÜM ÜST BOŞLUKLARI ÖLDÜREN KISIM */
    /* 1. Adım: Header'ı tamamen kapat ve yer kaplamasını engelle */
    header[data-testid="stHeader"] {
        visibility: hidden;
        height: 0%;
        display: none;
    }

    /* 2. Adım: Ana içerik alanındaki üst boşluğu sıfırla */
    .main .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        margin-top: 0rem !important;
    }

    /* 3. Adım: Streamlit'in otomatik eklediği 'deploy' barını gizle */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }

    /* Giriş ekranındaki kartı biraz daha yukarı taşımak istersen burayı kullanabilirsin */
    .login-spacer { margin-top: 50px; }

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
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {
        background: #00d2ff !important;
        border-bottom: 8px solid #0099cc !important;
    }
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {
        background: #ff4b5c !important;
        border-bottom: 8px solid #cc3344 !important;
    }
    div.stButton > button:active { transform: translateY(6px) !important; border-bottom: 2px solid transparent !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. Session State (Oturum ve Veri Yönetimi)
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
        st.markdown("<div style='margin-top: 100px;'></div>", unsafe_allow_html=True)
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        
        # Logo Kontrolü
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
        st.markdown("</div>", unsafe_allow_html=True)

# --- ANA DASHBOARD MANTIĞI ---
else:
    # Başlık
    st.markdown("<h1 style='text-align:center; color:white; font-weight:900; margin-top:20px;'>BULUTO SECURITY PRO</h1>", unsafe_allow_html=True)
    
    # Sidebar (Tüm Fonksiyonlar Burada)
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

    # Orta Panel
    _, main_col, _ = st.columns([1, 3.5, 1])
    
    with main_col:
        # Canlı Yayın Kartı
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<div class='label-tag'>CANLI KAMERA</div>", unsafe_allow_html=True)
        st.markdown("<div class='video-container'>GÖRÜNTÜ ANALİZ EDİLİYOR...</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # Tespit Alanı
        if st.session_state['active_request']:
            req = st.session_state['active_request']
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            st.markdown("<div class='label-tag'>TESPİT EDİLEN ARAÇ</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='plaka-bg'><div class='plaka-num'>{req['Plaka']}</div></div>", unsafe_allow_html=True)
            st.write(f"**Talep Zamanı:** {req['Saat']}")
            st.markdown("</div>", unsafe_allow_html=True)

            # Aksiyonlar
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