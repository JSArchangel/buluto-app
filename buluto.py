import streamlit as st
import pandas as pd
from datetime import datetime
import os
from PIL import Image

# 1. Sayfa Konfigürasyonu (Örnekteki gibi temiz ve geniş)
st.set_page_config(page_title="Buluto | Soft UI Dashboard", layout="wide")

# 2. ÖZEL CSS (Görseldeki "Tatlı" Arallüzü Yaratıyoruz)
st.markdown("""
    <style>
    /* Ana Arka Plan - Görseldeki Pembe-Mavi Gradyan */
    .stApp {
        background: linear-gradient(135deg, #fce4ec 0%, #e1f5fe 100%);
        color: #333;
    }
    
    /* Üst Bar Tasarımı */
    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 30px;
        background: rgba(255, 255, 255, 0.4);
        border-radius: 0 0 20px 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }

    /* Görseldeki "Beyaz Kart" Tasarımı */
    .info-card {
        background-color: #ffffff;
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        border: 1px solid rgba(0,0,0,0.02);
    }
    
    /* Kamera Vizörü (Görseldeki gibi kart içinde) */
    .camera-card {
        width: 100%;
        max-width: 700px;
        aspect-ratio: 16/9;
        margin: 0 auto;
        background-color: #f5f5f5;
        border-radius: 15px;
        display: flex;
        justify-content: center;
        align-items: center;
        border: 2px dashed #ddd;
    }

    /* Plaka ve Metinler */
    .plaka-text {
        font-family: 'Poppins', sans-serif;
        font-size: 32px;
        font-weight: bold;
        color: #1E90FF;
        letter-spacing: 2px;
    }
    .time-text {
        font-size: 14px;
        color: #888;
    }
    
    /* Buton Tasarımları (Kart gibi yumuşak) */
    div.stButton > button {
        border-radius: 15px !important;
        height: 3.5em !important;
        font-weight: bold !important;
        background-color: #ffffff !important;
        border: 1px solid rgba(0,0,0,0.05) !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05) !important;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 10px rgba(0,0,0,0.1) !important;
    }
    
    /* Streamlit'in standart elemanlarını gizle */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Oturum Durumu
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'active_request' not in st.session_state:
    st.session_state['active_request'] = {"Plaka": "34 XYZ 001", "Saat": "05:15:30"}

# --- GİRİŞ EKRANI (Aynı Tasarımla) ---
if not st.session_state['logged_in']:
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        st.markdown("<br><br><br><br>", unsafe_allow_html=True)
        if os.path.exists("logo.png"):
            st.image("logo.png", width=250)
        st.markdown("<div class='info-card'><h3 style='text-align:center;'>Giriş Paneli</h3>", unsafe_allow_html=True)
        user = st.text_input("Kullanıcı")
        pw = st.text_input("Şifre", type="password")
        if st.button("SİSTEME ERİŞ", use_container_width=True):
            if user == "admin" and pw == "buluto2024":
                st.session_state['logged_in'] = True
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- ANA DASHBOARD ---
else:
    # Üst Bilgi Çubuğu (Şeffaf kart gibi)
    st.markdown(f"""
    <div class="top-bar">
        <div style="font-size: 18px; font-weight: bold; color: #1E90FF;">BULUTO Security</div>
        <div style="color: #666;">● AKTİF | {datetime.now().strftime("%H:%M")}</div>
    </div>
    """, unsafe_allow_html=True)

    # Odak Alanı: Kamera (Üstte, Beyaz Kart İçinde)
    col_main_l, col_main_m, col_main_r = st.columns([1, 3, 1])
    
    with col_main_m:
        st.markdown("<div class='info-card'>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 18px; font-weight: bold; margin-bottom: 10px;'>Canlı Kamera Yayını</p>", unsafe_allow_html=True)
        st.markdown("""
        <div class="camera-card">
            <p style="color: #bbb; font-size: 14px;">LIVE FEED</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Karar Alanı: Plaka ve Butonlar (Altta)
    col_actions_l, col_actions_m, col_actions_r = st.columns([1, 2, 1])
    
    with col_actions_m:
        if st.session_state['active_request']:
            req = st.session_state['active_request']
            
            # Plaka Kartı
            st.markdown(f"""
            <div class="info-card" style="text-align: center;">
                <p class="time-text">Tespit Edilen Araç</p>
                <h1 class="plaka-text">{req['Plaka']}</h1>
                <p class="time-text">• {req['Saat']} •</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Buton Kartı (Görseldeki "Company Details" kartı gibi)
            st.markdown("<div class='info-card'>", unsafe_allow_html=True)
            st.markdown("<p style='font-weight: bold; margin-bottom: 15px;'>Giriş Kararı</p>", unsafe_allow_html=True)
            btn_col1, btn_col2 = st.columns(2)
            
            # Onay Butonu (Yumuşak yeşil gölge/metin)
            if btn_col1.button("✅ GİRİŞE İZİN VER", use_container_width=True):
                st.success(f"{req['Plaka']} girişine izin verildi.")
                st.session_state['active_request'] = None
                # Veritabanı işlemi buraya
            
            # Red Butonu (Yumuşak kırmızı gölge/metin)
            if btn_col2.button("❌ GİRİŞİ REDDET", use_container_width=True):
                st.warning(f"{req['Plaka']} girişi reddedildi.")
                st.session_state['active_request'] = None
            st.markdown("</div>", unsafe_allow_html=True)

    # Test Aracı Simülasyonu (Sidebar yerine altta bir kart)
    st.markdown("---")
    with st.expander("🛠️ Test Araçları (Kamera Simülasyonu)"):
        test_p = st.text_input("Test Plakası")
        if st.button("Yeni Araç Gönder", use_container_width=True):
            st.session_state['active_request'] = {"Plaka": test_p.upper(), "Saat": datetime.now().strftime("%H:%M:%S")}
            st.rerun()