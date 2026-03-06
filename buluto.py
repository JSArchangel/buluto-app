import streamlit as st
import os
from datetime import datetime

# 1. Sayfa Ayarları - Tarayıcı sekmesi ve geniş düzen
st.set_page_config(
    page_title="Buluto Security Pro",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS MASTER BLOCK - Görsel hataları ve beyaz barı yok eden kısım
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@700&family=Lexend:wght@800&display=swap');

    /* Genel Yazı Tipi */
    html, body, [class*="css"] { 
        font-family: 'Lexend', sans-serif !important; 
    }

    /* Arka Plan Degradesi */
    .stApp { 
        background: linear-gradient(180deg, #00c6ff 0%, #0072ff 100%); 
    }

    /* BEYAZ BARI VE STANDART BOŞLUKLARI ÖLDÜREN KISIM */
    .block-container { padding-top: 0rem !important; padding-bottom: 0rem !important; }
    header, footer, #MainMenu { visibility: hidden !important; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    
    /* GLASSMORPHISM KART YAPISI (Dolgun Arka Plan) */
    .glass-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 25px;
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2), inset 0 -5px 0 rgba(0, 0, 0, 0.1);
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.3);
    }

    /* VİDEO VİZÖRÜ */
    .video-container {
        width: 100%;
        height: 400px;
        background-color: #0f172a;
        border-radius: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #38bdf8;
        font-size: 20px;
        font-weight: bold;
        box-shadow: inset 0 0 60px rgba(0,0,0,0.8);
        border: 4px solid #f8fafc;
        margin-top: 10px;
    }

    /* PLAKA ARKA PLANI - KOYU VE DOLU */
    .plaka-bg {
        background: #0f172a; 
        border-radius: 20px;
        padding: 25px;
        margin: 20px auto;
        box-shadow: 0 10px 0 #000;
        display: flex;
        justify-content: center;
        align-items: center;
        min-width: 300px;
    }

    /* PLAKA YAZISI - HAFİF NEON VE TAM ORTALI */
    .plaka-num {
        font-family: 'Fira Code', monospace !important;
        font-size: 64px !important;
        font-weight: 700;
        color: #ffffff !important;
        letter-spacing: 10px; 
        padding-left: 10px; /* Simetri dengeleyici */
        text-shadow: 0 0 5px #fff, 0 0 15px #38bdf8;
        text-align: center;
        line-height: 1.2;
    }

    /* ETİKETLER */
    .label-tag {
        background: #38bdf8;
        color: #0f172a;
        padding: 6px 18px;
        border-radius: 12px;
        font-size: 13px;
        display: inline-block;
        margin-bottom: 12px;
        font-weight: 800;
        text-transform: uppercase;
    }

    /* 3D BUTON TASARIMLARI */
    div.stButton > button {
        border-radius: 22px !important;
        font-weight: 800 !important;
        height: 75px !important;
        border: none !important;
        color: white !important;
        font-size: 20px !important;
        transition: all 0.1s ease !important;
    }

    /* Onayla Butonu */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {
        background: #00d2ff !important;
        border-bottom: 8px solid #0099cc !important;
        box-shadow: 0 8px 15px rgba(0, 210, 255, 0.3) !important;
    }

    /* Reddet Butonu */
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {
        background: #ff4b5c !important;
        border-bottom: 8px solid #cc3344 !important;
        box-shadow: 0 8px 15px rgba(255, 75, 92, 0.3) !important;
    }

    div.stButton > button:active { 
        transform: translateY(6px) !important; 
        border-bottom: 2px solid transparent !important;
    }

    /* Giriş Ekranı Input Düzenlemesi */
    .stTextInput input {
        background-color: #f1f5f9 !important;
        border-radius: 15px !important;
        height: 50px !important;
        font-weight: 600 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. OTURUM YÖNETİMİ
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if 'active_request' not in st.session_state:
    st.session_state['active_request'] = {
        "Plaka": "34 BAA 001", 
        "Saat": datetime.now().strftime("%H:%M:%S")
    }

# --- A. GİRİŞ EKRANI SİMÜLASYONU ---
if not st.session_state['logged_in']:
    st.write("") # Üst boşluk dengeleyici
    _, login_col, _ = st.columns([1, 1.2, 1])
    
    with login_col:
        st.markdown("<div style='margin-top: 80px;'></div>", unsafe_allow_html=True)
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        
        # Logo Kontrolü
        if os.path.exists("logo.png"):
            st.image("logo.png", use_container_width=True)
        else:
            st.markdown("<h2 style='color:#0072ff'>BULUTO SECURITY</h2>", unsafe_allow_html=True)
        
        st.write("### Yönetici Paneli")
        user = st.text_input("Kullanıcı Adı", placeholder="admin")
        pw = st.text_input("Şifre", type="password", placeholder="••••••••")
        
        if st.button("SİSTEME GİRİŞ YAP", use_container_width=True):
            if user == "admin" and pw == "buluto2024":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("Hatalı Giriş Bilgileri!")
        
        st.markdown("</div>", unsafe_allow_html=True)

# --- B. ANA DASHBOARD EKRANI ---
else:
    # Başlık Alanı
    st.markdown("<h1 style='text-align:center; color:white; font-weight:900; margin-top:30px; letter-spacing:3px;'>BULUTO SECURITY PRO</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:rgba(255,255,255,0.8); font-weight:bold;'>YAPAY ZEKA DESTEKLİ PLAKA TANIMA SİSTEMİ</p>", unsafe_allow_html=True)

    # Ana İçerik Kolonları
    _, main_col, _ = st.columns([1, 4, 1])
    
    with main_col:
        # 1. Kamera Akışı Kartı
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<div class='label-tag'>🔴 CANLI KAMERA AKIŞI</div>", unsafe_allow_html=True)
        st.markdown("<div class='video-container'>SİSTEM AKTİF: ARAÇ BEKLENİYOR...</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # 2. Tespit Edilen Araç Kartı
        if st.session_state['active_request']:
            req = st.session_state['active_request']
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            st.markdown("<div class='label-tag'>🔍 SON TESPİT EDİLEN ARAÇ</div>", unsafe_allow_html=True)
            
            # Neon Plaka ve Dolu Arka Plan
            st.markdown(f"""
                <div class='plaka-bg'>
                    <div class='plaka-num'>{req['Plaka']}</div>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"<p style='color:#64748b; font-size:16px; font-weight:bold;'>Tespit Zamanı: {req['Saat']}</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            # 3. Aksiyon Butonları (Yan Yana)
            btn_col1, btn_col2 = st.columns(2)
            
            with btn_col1:
                if st.button("✅ BEYAZ LİSTE: ONAYLA", use_container_width=True):
                    st.success(f"{req['Plaka']} girişine izin verildi.")
                    st.session_state['active_request'] = None
                    # Buraya kapı açma sinyali (API) eklenebilir
            
            with btn_col2:
                if st.button("❌ KARA LİSTE: REDDET", use_container_width=True):
                    st.warning(f"{req['Plaka']} girişi engellendi!")
                    st.session_state['active_request'] = None

    # Sidebar - Simülasyon ve Bilgi Paneli
    with st.sidebar:
        if os.path.exists("logo.png"):
            st.image("logo.png")
        st.markdown("### 🛠️ SİSTEM ARAÇLARI")
        st.info("Kameradan plaka geldiğinde sistem otomatik olarak orta panele yansıtacaktır.")
        
        st.markdown("---")
        test_input = st.text_input("Plaka Simülasyonu", placeholder="Örn: 06 ANK 06")
        if st.button("Sistemi Tetikle"):
            if test_input:
                st.session_state['active_request'] = {
                    "Plaka": test_input.upper(),
                    "Saat": datetime.now().strftime("%H:%M:%S")
                }
                st.rerun()
        
        st.markdown("---")
        if st.button("Güvenli Çıkış"):
            st.session_state['logged_in'] = False
            st.rerun()