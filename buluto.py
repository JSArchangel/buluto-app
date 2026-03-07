import streamlit as st
import os
import sqlite3
from datetime import datetime

# 1. SAYFA AYARLARI
st.set_page_config(
    page_title="Buluto Security Pro",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. SQLITE VERİTABANI MOTORU
def get_db_connection():
    conn = sqlite3.connect('buluto_security.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS plaka_kayitlari (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plaka TEXT NOT NULL,
            zaman TEXT NOT NULL,
            durum TEXT NOT NULL
        );
    """)
    conn.commit()
    conn.close()

init_db()

# 3. SENİN ASIL TASARIMIN (CSS - BEYAZ BAR GİZLEME DAHİL)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@700&family=Lexend:wght@800&display=swap');

html, body, [class*="css"] {
    font-family: 'Lexend', sans-serif !important;
}

/* BEYAZ BARI VE MENÜLERİ YOK EDEN KISIM */
[data-testid="stHeader"] {display:none !important;}
footer {visibility:hidden !important;}
#MainMenu {visibility:hidden !important;}

.main .block-container{
    padding-top:0rem;
    padding-bottom:0rem;
    margin-top:-40px;
}

.stApp{
background: linear-gradient(180deg,#00c6ff 0%,#0072ff 100%);
overflow:hidden;
}

.sun{
position:fixed;
top:-120px;
right:-120px;
width:350px;
height:350px;
background: radial-gradient(circle,rgba(255,255,255,0.8),rgba(255,255,255,0));
filter:blur(40px);
z-index:0;
}

.cloud{
position:fixed;
left:-300px;
width:250px;
height:80px;
background:white;
opacity:0.6;
border-radius:100px;
filter:blur(1px);
animation:cloudMove linear infinite;
z-index:0;
}

.cloud:before,.cloud:after{
content:"";
position:absolute;
background:white;
border-radius:50%;
}

.cloud:before{
width:120px;
height:120px;
top:-50px;
left:20px;
}

.cloud:after{
width:100px;
height:100px;
top:-40px;
left:120px;
}

.cloud1{top:15%;animation-duration:40s;}
.cloud2{top:40%;animation-duration:55s;}
.cloud3{top:65%;animation-duration:70s;}

@keyframes cloudMove{
0%{transform:translateX(-300px);}
100%{transform:translateX(120vw);}
}

.glass-card{
background:rgba(255,255,255,0.92);
border-radius:25px;
padding:30px;
margin-bottom:25px;
box-shadow:0 20px 40px rgba(0,0,0,0.25);
text-align:center;
}

.video-container{
width:100%;
height:420px;
background:#0f172a;
border-radius:20px;
display:flex;
justify-content:center;
align-items:center;
color:#38bdf8;
font-weight:bold;
border:4px solid #f8fafc;
box-shadow:inset 0 0 50px rgba(0,0,0,0.8);
position:relative;
overflow:hidden;
}

.video-container:after{
content:"";
position:absolute;
width:100%;
height:3px;
background:#38bdf8;
top:0;
animation:scan 3s linear infinite;
}

@keyframes scan{
0%{top:0;}
100%{top:100%;}
}

.label-tag{
background:#38bdf8;
color:#0f172a;
padding:6px 18px;
border-radius:12px;
font-size:13px;
display:inline-block;
margin-bottom:12px;
font-weight:800;
}

.plaka-bg{
background:#0f172a;
border-radius:20px;
padding:25px;
margin:20px auto;
box-shadow:0 10px 0 #000;
display:flex;
justify-content:center;
}

.plaka-num{
font-family:'Fira Code',monospace !important;
font-size:48px !important;
font-weight:700;
color:#ffffff !important;
letter-spacing:8px;
text-shadow:
0 0 5px #fff,
0 0 10px #38bdf8,
0 0 20px #38bdf8,
0 0 40px #38bdf8;
}

div.stButton>button{
border-radius:22px !important;
font-weight:800 !important;
height:70px !important;
border:none !important;
color:white !important;
font-size:18px !important;
background:#ff5555 !important;
border-bottom:8px solid #cc4444 !important;
transition:0.15s;
}

div.stButton>button:hover{
transform:scale(1.05);
box-shadow:0 10px 25px rgba(0,0,0,0.4);
}

div.stButton>button:active{
transform:translateY(6px);
border-bottom:2px solid transparent;
}

.whatsapp-float{
position:fixed;
bottom:25px;
right:25px;
background:#25D366;
color:white;
border-radius:50px;
padding:16px 22px;
font-size:16px;
font-weight:800;
box-shadow:0 10px 25px rgba(0,0,0,0.3);
text-decoration:none;
z-index:9999;
}
</style>
""", unsafe_allow_html=True)

# GÖRSEL ELEMENTLER (GÜNEŞ VE BULUTLAR)
st.markdown("""
<div class="sun"></div>
<div class="cloud cloud1"></div>
<div class="cloud cloud2"></div>
<div class="cloud cloud3"></div>
""", unsafe_allow_html=True)

# 4. SESSION STATE
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'active_request' not in st.session_state:
    st.session_state.active_request = {"Plaka":"34 BAA 001","Saat":"05:40:12"}

# 5. GİRİŞ EKRANI
if not st.session_state.logged_in:
    _,c,_ = st.columns([1,1.2,1])
    with c:
        if os.path.exists("logo.png"):
            st.image("logo.png")
        st.markdown("### Yönetici Girişi")
        user = st.text_input("Kullanıcı Adı")
        pw = st.text_input("Şifre", type="password")
        if st.button("SİSTEMİ BAŞLAT", use_container_width=True):
            if user == "admin" and pw == "buluto2024":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Hatalı Kimlik Bilgileri")

# 6. ANA SİSTEM (Giriş Yapılınca Çalışan Dev Kısım)
else:
    # --- İŞTE O GERİ GELEN SIDEBAR ---
    with st.sidebar:
        if os.path.exists("logo.png"):
            st.image("logo.png")
        st.subheader("Simülasyon")
        sim_plaka = st.text_input("Plaka Manuel Giriş")
        if st.button("Kameraya Gönder"):
            if sim_plaka:
                st.session_state.active_request = {
                    "Plaka": sim_plaka.upper(),
                    "Saat": datetime.now().strftime("%H:%M:%S")
                }
                st.rerun()

        st.divider()
        st.subheader("Son Geçişler (DB)")
        
        # VERİTABANINDAN ÇEKME (SQLite)
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM plaka_kayitlari ORDER BY id DESC LIMIT 5")
        rows = cur.fetchall()
        for r in rows:
            st.write(f"🚗 {r['plaka']} - {r['durum']}")
        conn.close()

        if st.button("Güvenli Çıkış"):
            st.session_state.logged_in = False
            st.rerun()

    # ANA EKRAN BAŞLIĞI
    st.markdown("""
    <h1 style='text-align:center;color:white;font-weight:900;margin-top:20px;letter-spacing:2px;text-shadow:0 0 10px rgba(255,255,255,0.6),0 0 30px rgba(56,189,248,0.8);'>
    BULUTO SECURITY PRO
    </h1>
    """, unsafe_allow_html=True)

    _, main, _ = st.columns([1, 3.5, 1])
    with main:
        # KAMERA GÖRÜNTÜSÜ
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<div class='label-tag'>CANLI KAMERA</div>", unsafe_allow_html=True)
        st.markdown("<div class='video-container'>GÖRÜNTÜ ANALİZ EDİLİYOR...</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # PLAKA KARTI
        if st.session_state.active_request:
            req = st.session_state.active_request
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            st.markdown("<div class='label-tag'>TESPİT EDİLEN ARAÇ</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='plaka-bg'><div class='plaka-num'>{req['Plaka']}</div></div>", unsafe_allow_html=True)
            st.write("Tespit Zamanı:", req["Saat"])
            st.markdown("</div>", unsafe_allow_html=True)

            b1, b2 = st.columns(2)
            with b1:
                if st.button("✅ GİRİŞE İZİN VER", use_container_width=True):
                    # SQLite Kayıt
                    conn = get_db_connection()
                    conn.execute("INSERT INTO plaka_kayitlari (plaka, zaman, durum) VALUES (?, ?, ?)",
                               (req['Plaka'], datetime.now().strftime("%H:%M:%S"), "ONAYLANDI"))
                    conn.commit()
                    conn.close()
                    st.session_state.active_request = None
                    st.rerun()

            with b2:
                if st.button("❌ GİRİŞİ ENGELLE", use_container_width=True):
                    # SQLite Kayıt
                    conn = get_db_connection()
                    conn.execute("INSERT INTO plaka_kayitlari (plaka, zaman, durum) VALUES (?, ?, ?)",
                               (req['Plaka'], datetime.now().strftime("%H:%M:%S"), "REDDEDİLDİ"))
                    conn.commit()
                    conn.close()
                    st.session_state.active_request = None
                    st.rerun()

st.markdown("""
<a href="https://wa.me/905309965466" target="_blank" class="whatsapp-float">
📞 Acil Yardım
</a>
""", unsafe_allow_html=True)