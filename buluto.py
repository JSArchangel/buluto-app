import streamlit as st
import pandas as pd
import time
import base64

# 1. SAYFA AYARLARI
st.set_page_config(page_title="Buluto Pro", page_icon="☁️", layout="wide")

# O çok beğenilen Güvenli Tekno-Bulut Logosunu SVG olarak kodun içine gömelim (Base64)
def get_base64_logo(svg_string):
    encoded_string = base64.b64encode(svg_string.encode('utf-8')).decode('utf-8')
    return f"data:image/svg+xml;base64,{encoded_string}"

# Bu SVG, senin o kilitli ve server detaylı modern tasarımını içerir.
secure_cloud_logo_svg = """
<svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <path d="M100 10L10 50V130C10 170.667 40 190 100 190C160 190 190 170.667 190 130V50L100 10Z" fill="#1E90FF" fill-opacity="0.1"/>
  <path d="M185 55H195V65H185V55Z" fill="#1E90FF" fill-opacity="0.3"/>
  <path d="M185 70H195V80H185V70Z" fill="#1E90FF" fill-opacity="0.3"/>
  <path d="M185 85H195V95H185V85Z" fill="#1E90FF" fill-opacity="0.3"/>
  
  <path d="M70 120C70 111.716 76.7157 105 85 105C86.9922 105 88.8917 105.38 90.6323 106.075C93.3283 100.975 98.5866 97.5 105 97.5C114.15 97.5 121.5 104.85 121.5 114C121.5 114.503 121.47 115.001 121.41 115.493C126.21 116.388 130 120.547 130 125.625C130 131.631 125.131 136.5 119.125 136.5H85C76.7157 136.5 70 129.784 70 120Z" fill="#1E90FF"/>
  
  <path d="M100 120C100 114.477 104.477 110 110 110C115.523 110 120 114.477 120 120V125H100V120ZM122 125H98V140H122V125ZM110 130C108.895 130 108 130.895 108 132C108 133.105 108.895 134 110 134C111.105 134 112 133.105 112 132C112 130.895 111.105 130 110 130Z" fill="white"/>
  
  <text x="100" y="160" font-family="Arial, Helvetica, sans-serif" font-weight="bold" font-size="24" text-anchor="middle" fill="white">BULUTO</text>
  <text x="100" y="175" font-family="Arial, Helvetica, sans-serif" font-size="12" text-anchor="middle" fill="#00BFFF">SECURITY</text>
</svg>
"""

# Base64 logo linkini oluşturalım
logo_base64_url = get_base64_logo(secure_cloud_logo_svg)

# LOGO VE TASARIM (CSS) AYARLARI
st.markdown(f"""
    <style>
    /* Arka Plan: Açık Çelik Mavisi (#B0C4DE) */
    .stApp {{
        background-color: #B0C4DE;
    }}

    /* Sol Menü (Sidebar): Koyu Çelik Tonu */
    [data-testid="stSidebar"] {{
        background-color: #9db1cc;
    }}

    /* Logo Konumu ve Giriş Ekranı Düzeni */
    .login-container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 50px;
    }}
    .login-logo {{
        margin-bottom: 20px;
        filter: drop-shadow(0px 4px 6px rgba(0, 0, 0, 0.3)); /* Hafif gölge kurumsal hava katar */
    }}
    
    /* Butonlar: Canlı Mavi */
    .stButton>button {{
        border-radius: 20px;
        width: 100%;
        background-color: #4682B4; /* SteelBlue */
        color: white;
        border: none;
        font-weight: bold;
        transition: 0.3s;
    }}
    
    .stButton>button:hover {{
        background-color: #5f9ea0;
        color: white;
    }}

    /* Giriş kutusu */
    .stTextInput>div>div>input {{
        border-radius: 15px;
        background-color: rgba(255, 255, 255, 0.9);
    }}
    
    /* Yan Menü Logosu */
    [data-testid="stSidebar"] img {{
        margin-top: -20px;
        margin-bottom: 20px;
    }}
    </style>
    
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    """, unsafe_allow_html=True)

# --- GİRİŞ KONTROLÜ (LOGIN) ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def login():
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    st.image(logo_base64_url, width=150) # O fenasal logoyu buraya kocaman koyalım
    st.title("☁️ Buluto Giriş")
    
    with st.container():
        user = st.text_input("Kullanıcı Adı")
        pw = st.text_input("Şifre", type="password")
        if st.button("Giriş Yap"):
            if user == "admin" and pw == "buluto2024": # Şifren kalsın gardaşım
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("Hatalı kullanıcı adı veya şifre!")
    st.markdown('</div>', unsafe_allow_html=True)

# Eğer giriş yapılmadıysa sadece giriş ekranını göster
if not st.session_state['logged_in']:
    login()
else:
    # --- ANA UYGULAMA (Giriş Başarılıysa Burası Çalışır) ---
    st.sidebar.image(logo_base64_url, width=100) # Yan menüde de parlasın
    st.sidebar.title("☁️ Buluto Kontrol")
    if st.sidebar.button("Güvenli Çıkış"):
        st.session_state['logged_in'] = False
        st.rerun()
        
    sayfa = st.sidebar.selectbox("Gitmek İstediğin Yer:", ["Canlı Takip", "İstatistikler", "Ayarlar"])

    if sayfa == "Canlı Takip":
        st.title("☁️ BULUTO | Canlı Otomasyon")
        
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
                time.sleep(1) # Gerçekçilik katar :)
                if "34" in plaka:
                    st.success(f"✅ {plaka} İÇİN KAPI AÇILDI!")
                    st.balloons()
                else:
                    st.error(f"❌ {plaka} KAYITLI DEĞİL!")

        st.divider()
        
        # Tablo Kısmı
        st.subheader("📋 Son Giriş Yapan Araçlar")
        data = {
            "Saat": ["19:40", "19:45"],
            "Plaka": ["34BOS12", "06ANK06"],
            "Durum": ["Onaylandı", "Onaylandı"]
        }
        st.table(pd.DataFrame(data))

    elif sayfa == "İstatistikler":
        st.title("📊 Kullanım Verileri")
        st.write("Burada ileride hangi saatte kaç araç girmiş grafikle göreceğiz.")
        # Örnek grafik
        chart_data = pd.DataFrame({"Araç Sayısı": [10, 20, 15, 30, 25, 40]})
        st.line_chart(chart_data)

    elif sayfa == "Ayarlar":
        st.title("⚙️ Sistem Ayarları")
        st.write("Kullanıcı yetkileri ve sistem parametreleri.")