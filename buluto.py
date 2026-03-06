import streamlit as st
import pandas as pd
from datetime import datetime
import os
from PIL import Image

# 1. Sayfa Konfigürasyonu ( iOS Uygulaması gibi temiz)
st.set_page_config(page_title="Buluto | Smart Security PRO", layout="wide")

# 2. ÖZEL CSS (Cam ve Pastel Teması)
st.markdown("""
    <style>
    /* Google Fonts - Lexend */
    @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;600;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Lexend', sans-serif !important;
    }

    /* Arka Plan: image_0.png'daki gibi Soft Pembe-Mor Gradyan */
    .stApp {
        background: linear-gradient(135deg, #fce4ec 0%, #e1f5fe 100%);
        color: #1e3c72;
    }
    
    /* CAM (GLASS) HÜCRELER - image_6.png İlhamlı */
    .glass-bubble {
        background: rgba(255, 255, 255, 0.4);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 2px solid rgba(255, 255, 255, 0.6);
        border-radius: 35px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.05);
        text-align: center;
    }

    /* Kamera Vizörü (Cam içinde koyu alan) */
    .camera-viewport {
        width: 100%;
        max-width: 800px;
        aspect-ratio: 16/9;
        margin: 0 auto;
        background: rgba(0, 0, 0, 0.1);
        border-radius: 25px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #fff;
        font-weight: 300;
        letter-spacing: 2px;
        border: 2px solid rgba(255, 255, 255, 0.3);
    }

    /* Plaka Yazısı */
    .plaka-box {
        font-size: 52px;
        font-weight: 800;
        color: #1e3c72;
        letter-spacing: 5px;
        margin: 15px 0;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.05);
    }

    /* image_0.png'daki ON/RED BUTON TASARIMI (AYNISI) */
    div.stButton > button {
        border-radius: 30px !important; /* image_0.png gibi yuvarlak */
        height: 4.5em !important;
        font-weight: 700 !important;
        background: #ffffff !important; /* Dış beyaz kart */
        border: 1px solid rgba(0,0,0,0.05) !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08) !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase;
        font-size: 14px !important;
        letter-spacing: 1px;
    }
    div.stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.15) !important;
    }
    
    /* Buton İçindeki Pastel Gradyan Efekti */
    div.stButton > button:active {
        background: linear-gradient(90deg, #fce4ec 0%, #e1f5fe 100%) !important;
    }

    /* Streamlit Gereksizleri Gizle */
    header, footer, #MainMenu {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Oturum Durumu
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'active_request' not in st.session_state:
    st.session_state['active_request'] = {"Plaka": "34 BAA 001", "Saat": "05:40"}

# --- GİRİŞ EKRANI (Aynı Soft Tema) ---
if not st.session_state['logged_in']:
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("<div class='glass-bubble'>", unsafe_allow_html=True)
        if os.path.exists("logo.png"):
            st.image("logo.png", use_container_width=True)
        st.markdown("<h3 style='font-weight:800;'>Erişim Paneli</h3>", unsafe_allow_html=True)
        u = st.text_input("Kullanıcı")
        p = st.text_input("Şifre", type="password")
        if st.button("GİRİŞ YAP", use_container_width=True):
            if u == "admin" and p == "buluto2024":
                st.session_state['logged_in'] = True
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- ANA PANEL ---
else:
    # Üst Navigasyon (Pastel)
    st.markdown(f"""
    <div style="display: flex; justify-content: space-between; padding: 15px 40px;">
        <div style="font-weight: 800; font-size: 20px;">BULUTO SECURITY <span style="font-weight:300;">PRO</span></div>
        <div style="color: #666; background: rgba(255,255,255,0.4); padding: 5px 20px; border-radius: 20px; font-weight: 600;">
            ● CANLI_YAYIN_01
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_l, col_m, col_r = st.columns([1, 3.5, 1])
    
    with col_m:
        # 1. Balon: Kamera (Glass)
        st.markdown("<div class='glass-bubble'>", unsafe_allow_html=True)
        st.markdown("<p style='font-size:12px; margin:0;'>CAM_FRONT</p>", unsafe_allow_html=True)
        st.markdown("<div class='camera-viewport'>SİSTEM ANALİZ EDİLİYOR...</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # 2. Balon: Plaka Bilgisi (Glass)
        if st.session_state['active_request']:
            req = st.session_state['active_request']
            st.markdown(f"""
            <div class='glass-bubble'>
                <p style='color: #666; font-size: 14px; letter-spacing: 2px;'>TESPİT EDİLEN</p>
                <div class='plaka-box'>{req['Plaka']}</div>
                <p style='color: #888; font-size:12px;'>Kamera Tespit Saati: {req['Saat']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # 3. Buton Balonu: image_0.png Tasarımı (AYNISI)
            st.markdown("<div class='glass-bubble' style='padding: 15px;'>", unsafe_allow_html=True)
            st.markdown("<p style='font-weight: 800; margin-bottom: 15px;'>Giriş Kararı</p>", unsafe_allow_html=True)
            b_c1, b_c2 = st.columns(2)
            
            # Onay Butonu (Pastel Yeşil Metin/Hissiyat)
            with b_c1:
                if st.button("✅ GİRİŞE İZİN VER", use_container_width=True):
                    st.success("KAPI AÇILIYOR")
                    st.session_state['active_request'] = None
            
            # Red Butonu (Pastel Kırmızı Metin/Hissiyat)
            with b_c2:
                if st.button("❌ GİRİŞİ REDDET", use_container_width=True):
                    st.session_state['active_request'] = None
                    st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

    # Simülasyon (Sidebar)
    with st.sidebar:
        st.markdown("### Araç Test Paneli")
        t_p = st.text_input("Plaka Gir")
        if st.button("Simüle Et"):
            st.session_state['active_request'] = {"Plaka": t_p.upper(), "Saat": datetime.now().strftime("%H:%M")}
            st.rerun()