import streamlit as st
import pandas as pd
import time

# 1. SAYFA AYARLARI
st.set_page_config(page_title="Buluto Pro", page_icon="☁️", layout="wide")

# 2. iPHONE TAM EKRAN VE TASARIM (CSS) AYARLARI
st.markdown("""
    <style>
    .stApp { background-color: #B0C4DE; }
    [data-testid="stSidebar"] { background-color: #9db1cc; }
    .stButton>button {
        border-radius: 20px;
        width: 100%;
        background-color: #4682B4;
        color: white;
        font-weight: bold;
    }
    .stTextInput>div>div>input { border-radius: 15px; }
    </style>
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    """, unsafe_allow_html=True)

# --- GİRİŞ KONTROLÜ (LOGIN) ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def login():
    st.title("☁️ Buluto Giriş")
    with st.container():
        user = st.text_input("Kullanıcı Adı")
        pw = st.text_input("Şifre", type="password")
        if st.button("Giriş Yap"):
            if user == "admin" and pw == "buluto2024": # Şifreni buradan değiştirebilirsin kanka
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("Hatalı kullanıcı adı veya şifre!")

# Eğer giriş yapılmadıysa sadece giriş ekranını göster
if not st.session_state['logged_in']:
    login()
else:
    # --- ANA UYGULAMA (Giriş Başarılıysa Burası Çalışır) ---
    st.sidebar.title("☁️ Buluto Kontrol")
    if st.sidebar.button("Güvenli Çıkış"):
        st.session_state['logged_in'] = False
        st.rerun()
        
    sayfa = st.sidebar.selectbox("Gitmek İstediğin Yer:", ["Canlı Takip", "İstatistikler", "Ayarlar"])

    if sayfa == "Canlı Takip":
        st.title("☁️ BULUTO | Canlı Otomasyon")
        col1, col2, col3 = st.columns(3)
        col1.metric("Bugün Giren", "42 Araç", "+5%")
        col2.metric("Reddedilen", "3 Araç", "-2%")
        col3.metric("Sistem Yükü", "%12")

        st.divider()
        plaka = st.text_input("Plaka Manuel Sorgu:", placeholder="Örn: 34ABC123")
        if st.button("Sistemi Tetikle"):
            with st.spinner('Kontrol ediliyor...'):
                time.sleep(1)
                if "34" in plaka:
                    st.success(f"✅ {plaka} İÇİN KAPI AÇILDI!")
                    st.balloons()
                else:
                    st.error(f"❌ {plaka} KAYITLI DEĞİL!")

        st.divider()
        st.subheader("📋 Son Giriş Yapan Araçlar")
        data = {"Saat": ["19:40", "19:45"], "Plaka": ["34BOS12", "06ANK06"], "Durum": ["Onaylandı", "Onaylandı"]}
        st.table(pd.DataFrame(data))
    
    # (Diğer sayfalar buraya eklenebilir...)