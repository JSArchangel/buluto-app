import streamlit as st
import os
import sqlite3
from datetime import datetime

st.set_page_config(
    page_title="Buluto Security Pro",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------
# DATABASE
# ---------------------------

def get_db_connection():
    conn = sqlite3.connect("buluto_security.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS plaka_kayitlari(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        plaka TEXT,
        zaman TEXT,
        durum TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

# ---------------------------
# CSS
# ---------------------------

st.markdown("""
<style>

[data-testid="stHeader"] {display:none;}
footer {visibility:hidden;}

.stApp{
background: linear-gradient(180deg,#00c6ff 0%,#0072ff 100%);
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
}

.plaka-bg{
background:#0f172a;
border-radius:20px;
padding:25px;
margin:20px auto;
display:flex;
justify-content:center;
}

.plaka-num{
font-size:48px;
color:white;
letter-spacing:8px;
font-weight:bold;
}

.whatsapp-float{
position:fixed;
bottom:25px;
right:25px;
background:#25D366;
color:white;
border-radius:40px;
padding:15px 22px;
font-weight:800;
text-decoration:none;
box-shadow:0 10px 25px rgba(0,0,0,0.3);
z-index:9999;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# SESSION
# ---------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "active_request" not in st.session_state:
    st.session_state.active_request = None

# ---------------------------
# LOGIN
# ---------------------------

if not st.session_state.logged_in:

    col1,col2,col3 = st.columns([1,1.2,1])

    with col2:

        if os.path.exists("logo.png"):
            st.image("logo.png")

        st.subheader("Yönetici Girişi")

        user = st.text_input("Kullanıcı")
        pw = st.text_input("Şifre", type="password")

        if st.button("SİSTEMİ BAŞLAT", use_container_width=True):

            if user == "admin" and pw == "buluto2024":

                st.session_state.logged_in = True
                st.rerun()

            else:
                st.error("Hatalı giriş")

# ---------------------------
# DASHBOARD
# ---------------------------

else:

    st.markdown(
    "<h1 style='text-align:center;color:white;'>BULUTO SECURITY PRO</h1>",
    unsafe_allow_html=True
    )

    # SIDEBAR
    with st.sidebar:

        st.header("Kontrol Paneli")

        if os.path.exists("logo.png"):
            st.image("logo.png")

        st.subheader("Simülasyon")

        sim = st.text_input("Plaka gir")

        if st.button("Kameraya Gönder"):

            if sim:

                st.session_state.active_request = {
                    "Plaka": sim.upper(),
                    "Saat": datetime.now().strftime("%H:%M:%S")
                }

                st.rerun()

        st.divider()

        st.subheader("Son Geçişler")

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM plaka_kayitlari ORDER BY id DESC LIMIT 5")

        rows = cur.fetchall()

        for r in rows:

            icon = "✅" if r["durum"] == "ONAYLANDI" else "❌"

            st.write(f"{icon} {r['plaka']} | {r['zaman']}")

        conn.close()

        if st.button("Çıkış"):
            st.session_state.logged_in = False
            st.rerun()

    # MAIN AREA
    col1,main,col3 = st.columns([1,3,1])

    with main:

        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.write("CANLI KAMERA")
        st.markdown("<div class='video-container'>GÖRÜNTÜ ANALİZ EDİLİYOR...</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        if st.session_state.active_request:

            req = st.session_state.active_request

            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

            st.write("TESPİT EDİLEN ARAÇ")

            st.markdown(
                f"<div class='plaka-bg'><div class='plaka-num'>{req['Plaka']}</div></div>",
                unsafe_allow_html=True
            )

            st.write("Saat:", req["Saat"])

            st.markdown("</div>", unsafe_allow_html=True)

            c1,c2 = st.columns(2)

            with c1:

                if st.button("✅ GİRİŞE İZİN VER", use_container_width=True):

                    conn = get_db_connection()
                    cur = conn.cursor()

                    cur.execute(
                    "INSERT INTO plaka_kayitlari (plaka,zaman,durum) VALUES (?,?,?)",
                    (req["Plaka"], datetime.now().strftime("%H:%M:%S"), "ONAYLANDI")
                    )

                    conn.commit()
                    conn.close()

                    st.session_state.active_request = None
                    st.rerun()

            with c2:

                if st.button("❌ GİRİŞİ ENGELLE", use_container_width=True):

                    conn = get_db_connection()
                    cur = conn.cursor()

                    cur.execute(
                    "INSERT INTO plaka_kayitlari (plaka,zaman,durum) VALUES (?,?,?)",
                    (req["Plaka"], datetime.now().strftime("%H:%M:%S"), "REDDEDİLDİ")
                    )

                    conn.commit()
                    conn.close()

                    st.session_state.active_request = None
                    st.rerun()

# WHATSAPP BUTTON
st.markdown("""
<a href="https://wa.me/905309965466" target="_blank" class="whatsapp-float">
📞 Acil Yardım
</a>
""", unsafe_allow_html=True)