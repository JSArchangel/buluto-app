import streamlit as st
import os
import pandas as pd
from datetime import datetime
from PIL import Image

# 1. Sayfa Ayarları
st.set_page_config(page_title="Buluto Security | Onay Paneli", page_icon="🛡️", layout="wide")

# 2. Stil Ayarları
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: white; }
    .main-header { color: #1E90FF; font-size: 30px; font-weight: bold; text-align: center; }
    .stButton>button { border-radius: 8px; font-weight: bold; }
    /* Onay butonu yeşil, Red butonu kırmızı */
    div.stButton > button:first-child { background-color: #28a745; color: white; }
    div.stButton > button:last-child { background-color: #dc3545; color: white; }
    .status-box { padding: 15px; border-radius: 10px; border: 1px solid #333; background: #111; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# Oturum ve Veri Yönetimi
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'pending_requests' not in st.session_state:
    # Örnek olsun diye bir tane bekleyen araç ekleyelim
    st.session_state['pending_requests'] = [
        {"id": 1, "Plaka": "34 ABC 123", "Zaman": "04:35", "Not": "Ziyaretçi - Blok B"}
    ]
if 'approved_vehicles' not in st.session_state:
    st.session_state['approved_vehicles'] = []
if 'rejected_vehicles' not in st.session_state:
    st.session_state['rejected_vehicles'] = []

# --- GİRİŞ EKRANI ---
if not st.session_state['logged_in']:
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        if os.path.exists("logo.png"):
            st.image("logo.png", use_container_width=True)
        st.title("Güvenlik Onay Sistemi")
        user = st.text_input("Personel ID")
        pw = st.text_input("Şifre", type="password")
        if st.button("SİSTEMİ AÇ"):
            if user == "admin" and pw == "buluto2024":
                st.session_state['logged_in'] = True
                st.rerun()

# --- ANA SİSTEM ---
else:
    st.sidebar.title("🛡️ Buluto Kontrol")
    menu = st.sidebar.radio("Menü", ["🔔 Onay Bekleyenler", "🚗 İçerideki Araçlar", "❌ Reddedilenler", "🚪 Çıkış"])

    if menu == "🚪 Çıkış":
        st.session_state['logged_in'] = False
        st.rerun()

    st.markdown(f'<p class="main-header">KAYITSIZ ARAÇ YÖNETİM MERKEZİ</p>', unsafe_allow_html=True)

    if menu == "🔔 Onay Bekleyenler":
        st.subheader("⚠️ Giriş İzni Bekleyen Kayıtsız Araçlar")
        
        if not st.session_state['pending_requests']:
            st.info("Şu an onay bekleyen bir araç yok. Sistem tarıyor...")
        else:
            for req in st.session_state['pending_requests']:
                with st.container():
                    col_info, col_btn1, col_btn2 = st.columns([3, 1, 1])
                    with col_info:
                        st.markdown(f"""
                        <div class="status-box">
                            <b>Plaka:</b> {req['Plaka']} <br>
                            <b>Tespit Saati:</b> {req['Zaman']} <br>
                            <b>Detay:</b> {req['Not']}
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col_btn1:
                        if st.button(f"Girişi Onayla", key=f"app_{req['id']}"):
                            req['Onay_Zamani'] = datetime.now().strftime("%H:%M:%S")
                            st.session_state['approved_vehicles'].append(req)
                            st.session_state['pending_requests'].remove(req)
                            st.success(f"{req['Plaka']} içeri alındı.")
                            st.rerun()
                    
                    with col_btn2:
                        if st.button(f"Girişi Reddet", key=f"rej_{req['id']}"):
                            req['Red_Zamani'] = datetime.now().strftime("%H:%M:%S")
                            st.session_state['rejected_vehicles'].append(req)
                            st.session_state['pending_requests'].remove(req)
                            st.warning(f"{req['Plaka']} girişi reddedildi.")
                            st.rerun()

    elif menu == "🚗 İçerideki Araçlar":
        st.subheader("Onay Almış ve İçeride Olan Araçlar")
        if st.session_state['approved_vehicles']:
            df_app = pd.DataFrame(st.session_state['approved_vehicles'])
            st.table(df_app[['Plaka', 'Zaman', 'Onay_Zamani', 'Not']])
        else:
            st.info("İçeride manuel onaylı araç bulunmuyor.")

    elif menu == "❌ Reddedilenler":
        st.subheader("Güvenlik Nedeniyle Reddedilen Girişler")
        if st.session_state['rejected_vehicles']:
            df_rej = pd.DataFrame(st.session_state['rejected_vehicles'])
            st.table(df_rej[['Plaka', 'Zaman', 'Red_Zamani', 'Not']])
        else:
            st.info("Henüz reddedilen bir araç yok.")

    # Manuel Araç Ekleme (Test için - Kameradan geliyormuş gibi)
    with st.sidebar.expander("➕ Test: Kayıtsız Araç Simüle Et"):
        test_plaka = st.text_input("Test Plakası")
        if st.button("Kamera Algıladı"):
            new_id = len(st.session_state['pending_requests']) + len(st.session_state['approved_vehicles']) + 1
            st.session_state['pending_requests'].append({
                "id": new_id,
                "Plaka": test_plaka.upper(),
                "Zaman": datetime.now().strftime("%H:%M"),
                "Not": "Kamera tarafından algılandı."
            })
            st.rerun()