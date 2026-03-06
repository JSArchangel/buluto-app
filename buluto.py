import streamlit as st
import os
from datetime import datetime

# 1. Sayfa Konfigürasyonu
st.set_page_config(page_title="Buluto Pro", layout="wide")

# 2. ÖZEL CSS (Sadece senin istediğin o 3D butonlar ve cam baloncuklar)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@400;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Lexend', sans-serif !important;
    }

    /* ARKA PLAN: İstediğin o ferah mavi gradyan */
    .stApp {
        background: linear-gradient(180deg, #4facfe 0%, #00f2fe 100%);
    }
    
    /* CAM BALONCUKLAR (image_f8f07d.png gibi) */
    .glass-bubble {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 2px solid rgba(255, 255, 255, 0.4);
        border-radius: 30px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
    }

    /* KAMERA ALANI (Büyük ve Odak Noktası) */
    .camera-box {
        width: 100%;
        height: 350px;
        background: rgba(0, 0, 0, 0.1);
        border-radius: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    /* PLAKA YAZISI (Kameradan daha küçük ve dengeli) */
    .plaka-text {
        font-size: 32px !important; /* Boyut küçültüldü */
        font-weight: 800;
        color: white;
        letter-spacing: 4px;
        text-align: center;
    }

    /* 3D BUTONLAR (image_f8f3fd.png AYNISI) */
    /* Onay Butonu - Turkuaz 3D */
    div.stButton > button:first-child {
        background: #00bcd4 !important;
        border: none !important;
        border-bottom: 5px solid #008ba3 !important;
        border-radius: 12px !important;
        color: white !important;
        font-weight: 800 !important;
        height: 60px !important;
        box-shadow: 0 4px #008ba3 !important;
        transition: all 0.1s !important;
    }
    div.stButton > button:first-child:active {
        border-bottom: 1px solid #008ba3 !important;
        transform: translateY(4px) !important;
        box-shadow: none !important;
    }

    /* Red Butonu - Kırmızı/Pembe 3D */
    .st-emotion-cache-19rxjzo div:nth-child(2) button {
        background: #ff4b5c !important;
        border: none !important;
        border-bottom: 5px solid #d43d4c !important;
        border-radius: 12px !important;
        color: white !important;
        font-weight: 800 !important;
        height: 60px !important;
        box-shadow: 0 4px #d43d4c !important;
    }
    
    header, footer, #MainMenu {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Oturum ve Veri
if 'active_request' not in st.session_state:
    st.session_state['active_request'] = {"Plaka": "34 BAA 001", "Saat": "05:40:12"}

# --- ANA EKRAN ---
st.markdown("<br>", unsafe_allow_html=True)
col_l, col_m, col_r = st.columns([1, 4, 1])

with col_m:
    # Başlık
    st.markdown("<h2 style='color: white; font-weight: 800; text-align: center;'>BULUTO SECURITY PRO</h2>", unsafe_allow_html=True)
    
    # 1. Baloncuk: Kamera (BÜYÜK)
    st.markdown("<div class='glass-bubble'>", unsafe_allow_html=True)
    st.markdown("<div class='camera-box'>CANLI GÖRÜNTÜ AKTARILIYOR...</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # 2. Baloncuk: Plaka (KÜÇÜK VE DENGELİ)
    if st.session_state['active_request']:
        req = st.session_state['active_request']
        st.markdown("<div class='glass-bubble'>", unsafe_allow_html=True)
        st.markdown(f"<div class='plaka-text'>{req['Plaka']}</div>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align:center; color:white; font-size:12px; opacity:0.8;'>Giriş Saati: {req['Saat']}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # 3. Butonlar (3D TASARIM)
        c1, c2 = st.columns(2)
        with c1:
            if st.button("✅ ONAYLA VE AÇ", use_container_width=True):
                st.session_state['active_request'] = None
                st.rerun()
        with c2:
            if st.button("❌ GİRİŞİ ENGELLE", use_container_width=True):
                st.session_state['active_request'] = None
                st.rerun()

# Sidebar (Sadece Test İçin)
with st.sidebar:
    st.image("logo.png") if os.path.exists("logo.png") else st.write("LOGO")
    t_p = st.text_input("Plaka")
    if st.button("Simüle Et"):
        st.session_state['active_request'] = {"Plaka": t_p.upper(), "Saat": datetime.now().strftime("%H:%M")}
        st.rerun()