import streamlit as st
import os
import pandas as pd
from datetime import datetime
from PIL import Image

# 1. Sayfa Ayarları
st.set_page_config(page_title="Buluto | Araç Takip Sistemi", page_icon="🚗", layout="wide")

# 2. Stil Ayarları (Siyah Tema & Kurumsal Mavi)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: white; }
    .main-header { color: #1E90FF; font-size: 35px; font-weight: bold; text-align: center; }
    .stButton>button { width: 100%; background-color: #1E90FF; color: white; border-radius: 8px; font-weight: bold; }
    .metric-container { background: #111; padding: 20px; border-radius: 10px; border: 1px solid #333; }
    </style>
    """, unsafe_allow_html=True)

# Oturum Durumu
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'vehicle_logs' not in st.session_state:
    st.session_state['vehicle_logs'] = []

# --- GİRİŞ EKRANI ---
if not st.session_state['logged_in']:
    st.markdown('<br><br>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        if os.path.exists("logo.png"):
            st.image("logo.png", use_container_width=True)
        st.title("Araç Takip Sistemi Girişi")
        user = st.text_input("Personel ID")
        pw = st.text_input("Şifre", type="password")
        if st.button("SİSTEMİ AÇ"):
            if user == "admin" and pw == "buluto2024":
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("Hatalı Giriş!")

# --- ANA SİSTEM (ARAÇ GİRİŞ-ÇIKIŞ) ---
else:
    st.sidebar.title("🚗 Buluto Araç Takip")
    menu = st.sidebar.radio("İşlemler", ["Hızlı Kayıt", "Aktif Araçlar", "Geçmiş Kayıtlar", "Çıkış"])

    if menu == "Çıkış":
        st.session_state['logged_in'] = False
        st.rerun()

    st.markdown('<p class="main-header">BULUTO ARAÇ YÖNETİM PANELİ</p>', unsafe_allow_html=True)

    if menu == "Hızlı Kayıt":
        st.subheader("Yeni Araç Kaydı Oluştur")
        c1, c2 = st.columns(2)
        with c1:
            plaka = st.text_input("Araç Plakası (Örn: 34 ABC 123)").upper()
            surucu = st.text_input("Sürücü Adı Soyadı")
        with c2:
            islem_tipi = st.selectbox("İşlem Tipi", ["Giriş", "Çıkış"])
            notlar = st.text_area("Notlar (Yük, Ziyaret Sebebi vb.)")

        if st.button("KAYDI TAMAMLA"):
            yeni_kayit = {
                "Zaman": datetime.now().strftime("%H:%M:%S"),
                "Plaka": plaka,
                "Sürücü": surucu,
                "İşlem": islem_tipi,
                "Not": notlar
            }
            st.session_state['vehicle_logs'].insert(0, yeni_kayit)
            st.success(f"{plaka} plakalı aracın {islem_tipi} işlemi kaydedildi!")

    elif menu == "Aktif Araçlar":
        st.subheader("İçeride Bulunan Araçlar")
        # Basit bir mantık: Giriş yapmış ama çıkış yapmamışları burada gösterebiliriz
        df = pd.DataFrame(st.session_state['vehicle_logs'])
        if not df.empty:
            st.table(df[df['İşlem'] == "Giriş"])
        else:
            st.info("Şu an içeride araç bulunmuyor.")

    elif menu == "Geçmiş Kayıtlar":
        st.subheader("Günlük Hareket Kayıtları")
        if st.session_state['vehicle_logs']:
            df = pd.DataFrame(st.session_state['vehicle_logs'])
            st.dataframe(df, use_container_width=True)
            
            # Veriyi Excel/CSV olarak indir
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Raporu İndir (CSV)", data=csv, file_name="buluto_kayitlar.csv", mime="text/csv")
        else:
            st.warning("Henüz kayıt oluşturulmamış.")