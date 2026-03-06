import streamlit as st
import os
from PIL import Image

# 1. Sayfa Ayarları
st.set_page_config(page_title="Buluto Security | Dashboard", page_icon="🛡️", layout="wide")

# 2. Arka Plan ve Stil (Siyah Tema)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: white; }
    .main-header { color: #1E90FF; font-size: 35px; font-weight: bold; text-align: center; margin-bottom: 20px; }
    .stButton>button { width: 100%; background-color: #1E90FF; color: white; border-radius: 8px; height: 3em; font-weight: bold; }
    .login-box { max-width: 400px; margin: auto; padding: 20px; border: 1px solid #333; border-radius: 15px; background: #111; }
    </style>
    """, unsafe_allow_html=True)

# Oturum Durumu Kontrolü
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# --- GİRİŞ EKRANI ---
if not st.session_state['logged_in']:
    st.markdown('<br><br>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.5, 1])
    
    with col2:
        # Logo Gösterimi
        if os.path.exists("logo.png"):
            st.image("logo.png", use_container_width=True)
        
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.markdown('<p style="text-align:center; font-size:24px;">GÜVENLİ ERİŞİM</p>', unsafe_allow_html=True)
        
        user = st.text_input("Yönetici Kimliği", placeholder="Kullanıcı adı...")
        pw = st.text_input("Erişim Anahtarı", type="password", placeholder="Şifre...")
        
        if st.button("SİSTEME GİRİŞ YAP"):
            if user == "admin" and pw == "buluto2024":
                st.session_state['logged_in'] = True
                st.rerun() # BURASI ÇOK ÖNEMLİ: Sayfayı anında yeniler ve içeri alır.
            else:
                st.error("ERİŞİM REDDEDİLDİ: Hatalı Kimlik Bilgileri!")
        st.markdown('</div>', unsafe_allow_html=True)

# --- SİSTEM ANA EKRANI (DASHBOARD) ---
else:
    # Sol Menü
    st.sidebar.title("🛡️ Buluto Control")
    st.sidebar.info("Sistem Durumu: Çevrimiçi")
    menu = st.sidebar.radio("Menü Paneli", ["📊 Genel Bakış", "🔍 Güvenlik Taraması", "📝 Sistem Logları", "🚪 Çıkış Yap"])

    if menu == "🚪 Çıkış Yap":
        st.session_state['logged_in'] = False
        st.rerun()

    # İçerik Alanı
    st.markdown(f'<p class="main-header">BULUTO SECURITY MONITORING</p>', unsafe_allow_html=True)
    
    if menu == "📊 Genel Bakış":
        c1, c2, c3 = st.columns(3)
        c1.metric("Aktif Korumalar", "24/7", "AKTİF")
        c2.metric("Engellenen Tehdit", "1,842", "+12")
        c3.metric("CPU Kullanımı", "%14", "Stabil")
        
        st.subheader("Anlık Veri Trafiği")
        st.area_chart([20, 45, 30, 60, 80, 75, 90])

    elif menu == "🔍 Güvenlik Taraması":
        st.subheader("Hızlı Tarama Başlat")
        if st.button("Taramayı Başlat"):
            with st.spinner('Sistem çekirdeği taranıyor...'):
                import time
                time.sleep(2)
                st.success("Tarama Tamamlandı. Kritik bir tehdit bulunamadı.")

    elif menu == "📝 Sistem Logları":
        st.write("Son 3 Erişim Kaydı:")
        st.code("""
        [2026-03-06 04:30] - Admin girişi başarılı. (IP: 192.168.1.1)
        [2026-03-06 04:15] - Güvenlik duvarı kuralı güncellendi.
        [2026-03-06 03:50] - Port 80 üzerinde şüpheli hareket engellendi.
        """)