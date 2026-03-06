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

[data-testid="stHeader"] {display:none;}
footer {visibility:hidden;}
#MainMenu {visibility:hidden;}

html, body, [class*="css"]{
font-family:'Lexend',sans-serif !important;
}

.main .block-container{
padding-top:0rem;
margin-top:-40px;
}

/* BACKGROUND */

.stApp{
background: linear-gradient(180deg,#00c6ff 0%,#0072ff 100%);
}

/* SUN */

.sun{
position:fixed;
top:-100px;
right:-100px;
width:300px;
height:300px;
background:radial-gradient(circle,rgba(255,255,255,0.8),rgba(255,255,255,0));
filter:blur(50px);
z-index:0;
}

/* CLOUD */

.cloud{
position:fixed;
left:-300px;
width:250px;
height:80px;
background:white;
opacity:0.5;
border-radius:100px;
animation:cloudMove linear infinite;
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

.cloud1{top:20%;animation-duration:140s;}
.cloud2{top:45%;animation-duration:200s;}
.cloud3{top:70%;animation-duration:240s;}

@keyframes cloudMove{
0%{transform:translateX(-300px);}
100%{transform:translateX(120vw);}
}

/* CARD */

.glass-card{
background:rgba(255,255,255,0.92);
border-radius:25px;
padding:30px;
margin-bottom:25px;
box-shadow:0 20px 40px rgba(0,0,0,0.25);
text-align:center;
}

/* CAMERA */

.video-container{
width:100%;
height:420px;
background:#0f172a;
border-radius:20px;
position:relative;
overflow:hidden;
display:flex;
align-items:center;
justify-content:center;
color:#38bdf8;
font-weight:bold;
border:4px solid white;
}

/* SCAN LINE */

.video-container:after{
content:"";
position:absolute;
width:100%;
height:3px;
background:#38bdf8;
animation:scan 3s linear infinite;
}

@keyframes scan{
0%{top:0;}
100%{top:100%;}
}

/* AI BOX */

.ai-box{
position:absolute;
width:200px;
height:80px;
border:3px solid #38bdf8;
box-shadow:0 0 20px #38bdf8;
animation:pulse 2s infinite;
}

@keyframes pulse{
0%{opacity:0.6}
50%{opacity:1}
100%{opacity:0.6}
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
font-family:'Fira Code',monospace;
font-size:64px;
letter-spacing:10px;
color:white;
text-shadow:
0 0 5px white,
0 0 15px #38bdf8,
0 0 30px #38bdf8;
}

/* BUTTON */

div.stButton>button{
border-radius:20px !important;
height:70px;
font-weight:800;
background:#ff5555;
border-bottom:8px solid #cc4444;
color:white;
transition:0.15s;
}

div.stButton>button:hover{
transform:scale(1.05);
}

/* BARRIER */

.barrier{
width:100%;
height:20px;
background:#222;
border-radius:10px;
position:relative;
margin-top:20px;
}

.barrier-arm{
width:60%;
height:8px;
background:red;
position:absolute;
top:6px;
left:20%;
transform-origin:left center;
transition:transform 1s;
}

.barrier-open{
transform:rotate(-60deg);
}

.status{
color:white;
text-align:center;
margin-bottom:10px;
font-size:14px;
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
if 'barrier' not in st.session_state:
    st.session_state.barrier=False

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
                st.error("Hatalı giriş")

else:

    st.markdown("""
<h1 style='text-align:center;color:white;font-weight:900;'>
BULUTO SECURITY PRO
</h1>
""",unsafe_allow_html=True)

    st.markdown("""
<div class="status">
🟢 Kamera Online | 🟢 AI Detection Aktif | 🟢 Sistem Stabil
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

        st.markdown("<div class='video-container'>",unsafe_allow_html=True)

        st.markdown("<div class='ai-box'></div>",unsafe_allow_html=True)

        st.markdown("GÖRÜNTÜ ANALİZ EDİLİYOR...")

        st.markdown("</div>",unsafe_allow_html=True)

        st.markdown("</div>",unsafe_allow_html=True)

        if st.session_state.active_request:

            req=st.session_state.active_request

            st.markdown("<div class='glass-card'>",unsafe_allow_html=True)

            st.markdown("<div class='plaka-bg'><div class='plaka-num'>{}</div></div>".format(req["Plaka"]),unsafe_allow_html=True)

            st.write("Talep Zamanı:",req["Saat"])

            st.markdown("</div>",unsafe_allow_html=True)

            b1,b2=st.columns(2)

            with b1:

                if st.button("✅ GİRİŞE İZİN VER",use_container_width=True):

                    st.session_state.history.append(req)
                    st.session_state.active_request=None
                    st.session_state.barrier=True
                    st.rerun()

            with b2:

                if st.button("❌ GİRİŞİ ENGELLE",use_container_width=True):

                    st.session_state.active_request=None
                    st.session_state.barrier=False
                    st.rerun()

        arm="barrier-arm barrier-open" if st.session_state.barrier else "barrier-arm"

        st.markdown(f"""
<div class="barrier">
<div class="{arm}"></div>
</div>
""",unsafe_allow_html=True)