import streamlit as st
import pandas as pd
import time
import random

# 1. SAYFA AYARLARI
st.set_page_config(page_title="Buluto Pro", page_icon="☁️", layout="wide")

# 2. iPHONE TAM EKRAN VE TASARIM (CSS) AYARLARI
st.markdown("""
    <style>
    /* Arka Plan: Açık Çelik Mavisi (#B0C4DE) */
    .stApp {
        background-color: #B0C4DE;
    }

    /* Sol Menü (Sidebar): Bir tık daha koyu çelik tonu */
    [data-testid="stSidebar"] {
        background-color: #9db1cc;
    }

    /* Kartlar ve Yazı Alanları: Okunabilirlik için hafif şeffaf beyaz dokunuş */
    .stMetric, .stTable {
        background-color: rgba(255, 255, 255, 0.4);
        padding: 15px;
        border-radius: 15px;
    }

    /* Butonlar: Canlı Mavi */
    .stButton>button {
        border-radius: 20px;
        width: 100%;
        background-color: #4682B4; /* SteelBlue */
        color: white;
        border: none;
        font-weight: bold;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #5f9ea0;
        color: white;
    }

    /* Giriş kutusu */
    .stTextInput>div>div>input {
        border-radius: 15px;
        background-color: rgba(255, 255, 255, 0.9);
    }
    </style>
    
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    """, unsafe_allow_html=True)

# --- SOL MENÜ (SIDEBAR) ---
st.sidebar.title("☁️ Buluto Kontrol")
st.sidebar.info("Sistem Durumu: Çevrimiçi ✅")
sayfa = st.sidebar.selectbox("Gitmek İstediğin Yer:", ["Canlı Takip", "İstatistikler", "Ayarlar"])

if sayfa == "Canlı Takip":
    st.title("☁️ BULUTO | Canlı Otomasyon Merkezi")
    
    # Üst tarafa özet kutucukları (Metric)
    col1, col2, col3 = st.columns(3)
    col1.metric("Bugün Giren", "42 Araç", "+5%")
    col2.metric("Reddedilen", "3 Araç", "-2%")
    col3.metric("Sistem Yükü", "%12")

    st.divider()

    # Plaka Sorgulama Alanı
    plaka = st.text_input("Plaka Manuel Sorgu:", placeholder="Örn: 34ABC123")
    if st.button("Sistemi Tetikle"):
        with st.spinner('Veritabanı kontrol ediliyor...'):
            time.sleep(1)
            if "34" in plaka:
                st.success(f"✅ {plaka} İÇİN KAPI AÇILDI!")
                st.balloons()
            else:
                st.error(f"❌ {plaka} KAYITLI DEĞİL!")

    st.divider()
    
    # Tablo Kısmı
    st.subheader("📋 Son Giriş Yapan Araçlar")
    data = {
        "Saat": ["19:40", "19:45", "19:50", "19:55"],
        "Plaka": ["34BOS12", "06ANK06", "35IZM35", "34BUL01"],
        "Durum": ["Onaylandı", "Onaylandı", "Reddedildi", "Onaylandı"]
    }
    st.table(pd.DataFrame(data))

elif sayfa == "İstatistikler":
    st.title("📊 Kullanım Verileri")
    chart_data = pd.DataFrame({"Araç Sayısı": [10, 20, 15, 30, 25, 40]})
    st.line_chart(chart_data)

elif sayfa == "Ayarlar":
    st.title("⚙️ Sistem Ayarları")
    st.write("Kullanıcı yetkileri ve sistem parametreleri.")