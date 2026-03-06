import streamlit as st
import os
from datetime import datetime

st.set_page_config(
    page_title="Buluto Security Pro",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@700&family=Lexend:wght@800&display=swap');

html, body, [class*="css"] {
    font-family: 'Lexend', sans-serif !important;
}

[data-testid="stHeader"] {display:none;}
footer {visibility:hidden;}
#MainMenu {visibility:hidden;}

.main .block-container{
    padding-top:0rem;
    padding-bottom:0rem;
    margin-top:-40px;
}

.stApp{
background: linear-gradient(180deg,#00c6ff 0%,#0072ff 100%);
overflow:hidden;
}

/* SUN EFFECT */

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

/* CLOUDS */

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

.cloud1{top:15%;animation-duration:120s;}
.cloud2{top:40%;animation-duration:160s;}
.cloud3{top:65%;animation-duration:200s;}

@keyframes cloudMove{
0%{transform:translateX(-300px);}
100%{transform:translateX(120vw);}
}

/* GLASS CARD */

.glass-card{
background:rgba(255,255,255,0.92);
border-radius:25px;
padding:30px;
margin-bottom:25px;
box-shadow:0 20px 40px rgba(0,0,0,0.25);
text-align:center;
}

/* VIDEO */

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

/* SCANNER */

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

/* LABEL */

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

/* PLATE */

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
font-size:64px !important;
font-weight:700;
color:#ffffff !important;
letter-spacing:10px;
text-shadow:
0 0 5px #fff,
0 0 10px #38bdf8,
0 0 20px #38bdf8,
0 0 40px #38bdf8;
}

/* BUTTON */

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

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="sun"></div>
<div class="cloud cloud1"></div>
<div class="cloud cloud2"></div>
<div class="cloud cloud3"></div>
""", unsafe_allow_html=True)

if 'logged_in' not in st.session_state:
    st.session_state.logged_in=False
if 'active_request' not in st.session_state:
    st.session_state.active_request={"Plaka":"34 BAA 001","Saat":"05:40:12"}
if 'history' not in st.session_state:
    st.session_state.history=[]

if not st.session_state.logged_in:

    _,c,_=st.columns([1,1.2,1])

    with c:

        if os.path.exists("logo.png"):
            st.image("logo.png")

        st.markdown("### Yönetici Girişi")

        user=st.text_input("Kullanıcı Adı")
        pw=st.text_input("Şifre",type="password")

        if st.button("SİSTEMİ BAŞLAT",use_container_width=True):

            if user=="admin" and pw=="buluto2024":
                st.session_state.logged_in=True
                st.rerun()
            else:
                st.error("Hatalı Kimlik Bilgileri")

else:

    st.markdown("""
<h1 style='
text-align:center;
color:white;
font-weight:900;
margin-top:20px;
letter-spacing:2px;
text-shadow:0 0 10px rgba(255,255,255,0.6),0 0 30px rgba(56,189,248,0.8);
'>
BULUTO SECURITY PRO
</h1>
""",unsafe_allow_html=True)

    st.markdown("""
<div style='text-align:center;color:white;font-size:14px;margin-bottom:20px;'>
🟢 Kamera Bağlı | 🟢 AI Analiz Aktif | 🟢 Sistem Stabil
</div>
""",unsafe_allow_html=True)

    with st.sidebar:

        if os.path.exists("logo.png"):
            st.image("logo.png")

        st.subheader("Simülasyon")

        sim=st.text_input("Plaka Gir")

        if st.button("Kameraya Gönder"):

            if sim:
                st.session_state.active_request={
                "Plaka":sim.upper(),
                "Saat":datetime.now().strftime("%H:%M:%S")
                }
                st.rerun()

        st.subheader("Son Geçişler")

        for i in st.session_state.history[-5:]:
            st.write(i["Saat"],"-",i["Plaka"])

        if st.button("Çıkış"):
            st.session_state.logged_in=False
            st.rerun()

    _,main,_=st.columns([1,3.5,1])

    with main:

        st.markdown("<div class='glass-card'>",unsafe_allow_html=True)

        st.markdown("<div class='label-tag'>CANLI KAMERA</div>",unsafe_allow_html=True)

        st.markdown("<div class='video-container'>GÖRÜNTÜ ANALİZ EDİLİYOR...</div>",unsafe_allow_html=True)

        st.markdown("</div>",unsafe_allow_html=True)

        if st.session_state.active_request:

            req=st.session_state.active_request

            st.markdown("<div class='glass-card'>",unsafe_allow_html=True)

            st.markdown("<div class='label-tag'>TESPİT EDİLEN ARAÇ</div>",unsafe_allow_html=True)

            st.markdown(f"<div class='plaka-bg'><div class='plaka-num'>{req['Plaka']}</div></div>",unsafe_allow_html=True)

            st.write("Talep Zamanı:",req["Saat"])

            st.markdown("</div>",unsafe_allow_html=True)

            b1,b2=st.columns(2)

            with b1:
                if st.button("✅ GİRİŞE İZİN VER",use_container_width=True):

                    st.session_state.history.append(req)

                    st.session_state.active_request=None

                    st.rerun()

            with b2:
                if st.button("❌ GİRİŞİ ENGELLE",use_container_width=True):

                    st.session_state.active_request=None

                    st.rerun()