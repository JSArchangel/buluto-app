import streamlit as st
import pandas as pd
from datetime import datetime
import os

# 1. Sayfa Konfigürasyonu
st.set_page_config(page_title="Buluto Security | Dashboard", layout="wide")

# 2. ÖZEL CSS (Arayüzü baştan yaratıyoruz)
st.markdown("""
    <style>
    /* Ana Ekranı Siyah ve Sabit Yap */
    .stApp {
        background-color: #060606;
        color: #ffffff;
    }
    
    /* Üst Bar Tasarımı */
    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 30px;
        background: rgba(255, 255, 255, 0.03);
        border-bottom: 1px solid rgba(30, 144, 255, 0.2);
    }

    /* Kamera Vizörü (Merkez Alan) */
    .camera-viewport {
        width: 100%;
        max-width: 800px;
        aspect-ratio: 16/9;
        margin: 30px auto;
        border: 2px solid #1E90FF;
        border-radius: 10px;
        background: #111;
        position: relative;
        box-shadow: 0 0 30px rgba(30, 144, 255, 0.1);
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
    }

    /* Vizör Köşe Çizgileri (Taktiksel Görünüm) */
    .corner {
        position: absolute;
        width: 20px;
        height: 20px;
        border: 2px solid #1E90FF;
    }
    .top-left { top: 10px; left: 10px; border-right: none; border-bottom: none; }
    .top-right { top: 10px; right: 10px; border-left: none; border-bottom: none; }
    .bottom-left { bottom: 10px; left: 10px; border-right: none; border-top: none; }
    .bottom-right { bottom: 10px; right: 10px; border-left: none; border-top: none; }

    /* Buton Grubu Konumu */
    .action-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: -10px;
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
    st.session_state['active_request'] = {"Plaka": "34 BAA 001", "Saat": datetime.now().strftime("%H:%M:%S")}

# --- GİRİŞ EKRANI ---
if not st.session_state['logged_in']:
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        if os.path.exists("logo.png"):
            st.image("logo.png", use_container_width=True)
        user = st.text_input("Sistem Yetkilisi")
        pw = st.text_input("Erişim Anahtarı", type="password")
        if st.button("SİSTEMİ BAŞLAT"):
            if user == "admin" and pw == "buluto2024":
                st.session_state['logged_in'] = True
                st.rerun()

# --- ANA DASHBOARD ---
else:
    # Üst Bilgi Çubuğu
    st.markdown(f"""
    <div class="top-bar">
        <div style="font-size: 20px; font-weight: bold; color: #1E90FF;">BULUTO COMMAND</div>
        <div style="color: #00ff00; font-family: monospace;">● SYSTEM ACTIVE | {datetime.now().strftime("%H:%M")}</div>
    </div>
    """, unsafe_allow_html=True)

    # ANA VİZÖR (Kamera Alanı)
    st.markdown("""
    <div class="camera-viewport">
        <div class="corner top-left"></div>
        <div class="corner top-right"></div>
        <div class="corner bottom-left"></div>
        <div class="corner bottom-right"></div>
        <div style="text-align: center; color: #333;">
            <p style="font-size: 24px; letter-spacing: 5px;">LIVE VIDEO FEED</p>
            <p style="font-size: 12px;">WAITING FOR DETECTION...</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Karar Butonları ve Bilgi Alanı
    col_l, col_m, col_r = st.columns([1, 2, 1])
    
    with col_m:
        if st.session_state['active_request']:
            req = st.session_state['active_request']
            st.markdown(f"""
            <div style="text-align: center; margin-bottom: 20px;">
                <h1 style="font-family: 'Courier New'; letter-spacing: 3px; color: #1E90FF; margin-bottom: 0;">{req['Plaka']}</h1>
                <p style="color: #888; margin-top: 0;">Giriş Talebi Tespit Edildi • {req['Saat']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            btn_col1, btn_col2 = st.columns(2)
            if btn_col1.button("✅ GİRİŞE İZİN VER", use_container_width=True):
                st.success("KAPI AÇILIYOR...")
                st.session_state['active_request'] = None
                # Buraya veritabanı kaydı gelecek
            
            if btn_col2.button("❌ GİRİŞİ REDDET", use_container_width=True):
                st.error("ERİŞİM REDDEDİLDİ.")
                st.session_state['active_request'] = None

    # Alt Bilgi Listesi (Sidebar yerine sadeleştirilmiş)
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #444; font-size: 12px;'>Buluto Security Systems v2.0 - Encrypted Connection</p>", unsafe_allow_html=True)

    # Simülasyon Butonu (Sağ Altta Gizli)
    with st.expander("Sistem Araçları"):
        new_p = st.text_input("Test Plakası")
        if st.button("Kamera Algıla"):
            st.session_state['active_request'] = {"Plaka": new_p.upper(), "Saat": datetime.now().strftime("%H:%M:%S")}
            st.rerun()