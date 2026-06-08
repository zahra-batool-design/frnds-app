import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
import os
import time
import random

# ========================= CONFIG =========================
st.set_page_config(
    page_title="Birthday Universe PRO MAX",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BASE = os.path.dirname(__file__)

# ========================= GLOBAL CSS =========================
st.markdown("""
<style>

.stApp {
    background: radial-gradient(circle,#1a001a,#000000,#000000);
    color:white;
}

/* glowing text */
.glow {
    text-shadow: 0 0 10px #ff2e63,
                 0 0 20px #ff2e63,
                 0 0 40px #ff2e63;
}

/* floating hearts */
.heart-float {
    position: fixed;
    animation: floatUp 12s linear infinite;
    font-size: 20px;
    opacity: 0.6;
}

@keyframes floatUp {
    0% {transform: translateY(100vh);}
    100% {transform: translateY(-200px);}
}

/* glass card */
.glass {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    margin: 10px;
}

</style>
""", unsafe_allow_html=True)

# ================= FLOATING HEARTS ENGINE =================
for i in range(20):
    st.markdown(
        f"<div class='heart-float' style='left:{random.randint(0,100)}%'>❤️</div>",
        unsafe_allow_html=True
    )

# ================= TABS =================
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["🏠 Home", "❤️ Heart", "💌 Letter", "📸 Memories", "🎉 Celebration"]
)

# =========================================================
# TAB 1 - HOME (EXPANDED)
# =========================================================
with tab1:

    st.markdown("""
    <style>
    .title{
        text-align:center;
        font-size:80px;
        color:#ff2e63;
        font-weight:900;
        animation: glow 2s infinite alternate;
    }

    @keyframes glow {
        from {transform:scale(1);}
        to {transform:scale(1.08);}
    }

    .box{
        background:rgba(255,255,255,0.06);
        padding:30px;
        border-radius:20px;
        margin-top:20px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='title glow'>💖 HAPPY BIRTHDAY DEAR 💖</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='box'>
    ✨ Welcome to your personal birthday universe ✨<br><br>

    💖 You are special<br>
    🌟 You are appreciated<br>
    🎂 You are celebrated<br>
    ❤️ You are valued deeply<br>
    🎉 Today is YOUR day
    </div>
    """, unsafe_allow_html=True)

    st.balloons()
    st.snow()

    # extra filler content (real feature expansion)
    st.markdown("## 🎁 Birthday Wishes For loved once💞😸")

    wishes = [
        "May your life shine brighter than stars ✨",
        
    ]

    for w in wishes:
        st.markdown(f"• {w}")

# =========================================================
# TAB 2 - HEART (ADVANCED 3D STYLE)
# =========================================================
with tab2:

    st.markdown("""
    <style>
    .heart {
        margin:auto;
        width:250px;
        height:250px;
        background:#ff1744;
        transform:rotate(-45deg);
        box-shadow:0 0 80px #ff1744;
        animation:pulse 1.2s infinite;
    }

    .heart:before,.heart:after{
        content:"";
        width:250px;
        height:250px;
        background:#ff1744;
        border-radius:50%;
        position:absolute;
    }

    .heart:before{top:-125px;}
    .heart:after{left:125px;}

    .name{
        position:absolute;
        transform:rotate(45deg);
        top:40%;
        left:20%;
        font-size:30px;
        color:white;
        font-weight:bold;
    }

    @keyframes pulse {
        0% {transform:rotate(-45deg) scale(1);}
        50% {transform:rotate(-45deg) scale(1.15);}
        100% {transform:rotate(-45deg) scale(1);}
    }

    .center {
        display:flex;
        justify-content:center;
        margin-top:120px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='glow' style='text-align:center;'>❤️ That's For You G ❤️</h1>", unsafe_allow_html=True)

    st.markdown("<div class='center'><div class='heart'><div class='name'>DEAR</div></div></div>", unsafe_allow_html=True)

    st.markdown("## 💖 Messages.....")
    msgs = [
        "You are important ❤️",
        
    ]

    for m in msgs:
        st.markdown(f"✔ {m}")

    try:
        st.audio(open("song.mp3","rb").read())
    except:
        st.warning("Add song.mp3")

# =========================================================
# TAB 3 - LETTER (LONG VERSION)
# =========================================================
with tab3:

    st.markdown("""
    <style>
    .letter{
        background:rgba(255,255,255,0.06);
        padding:40px;
        border-radius:25px;
        line-height:2;
        font-size:18px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("## 💌 LETTER ")

    st.markdown("""
    <div class='letter'>
    Dear frnd ❤️<br><br>

    I don’t know how to perfectly express this feeling.<br><br>

    You are someone very special in my life.<br>
    Someone who brings happiness and peace.<br><br>

    I appreciate your kindness.<br>
    I appreciate your presence.<br><br>

    💖 You are not just a friend — you are a blessing 💖<br><br>

    Happy Birthday 🎂
    </div>
    """, unsafe_allow_html=True)

    

    st.balloons()


# =========================================================
# TAB 4 - MEMORIES (FINAL WORKING VERSION)
# =========================================================
with tab4:

    import base64

    st.markdown("## 📸 Memories Universe 💖")

    # =====================================================
    # LOAD IMAGES
    # =====================================================
    images = [
        os.path.join(BASE, f"img{i}.jpg")
        for i in range(1, 13)
    ]
    images = [img for img in images if os.path.exists(img)]

    if not images:
        st.error("Add img1.jpg to img12.jpg in folder")
    else:

        # =====================================================
        # 🎵 MUSIC
        # =====================================================
        st.markdown("### 🎵 Memories Song")

        try:
            st.audio(open(os.path.join(BASE, "memories_song.mp3"), "rb").read())
        except:
            st.warning("⚠️ Add memories_song.mp3")

        st.markdown("---")

        # =====================================================
        # 1️⃣ LEFT → RIGHT MOVING FRAME GALLERY (FIXED)
        # =====================================================
        st.markdown("### 🎞 Moving Frames Gallery")

        def img_to_base64(path):
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()

        imgs_html = "".join([
            f'<img src="data:image/jpg;base64,{img_to_base64(img)}"/>'
            for img in images
        ])

        html_code = f"""
        <style>
        .slider {{
            width:100%;
            overflow:hidden;
            border-radius:20px;
            white-space:nowrap;
        }}

        .track {{
            display:inline-block;
            animation: scroll 15s linear infinite;
        }}

        .track img {{
            width:200px;
            height:150px;
            margin:10px;
            border-radius:15px;
            box-shadow:0 0 20px #ff2e63;
        }}

        @keyframes scroll {{
            0% {{ transform: translateX(0); }}
            100% {{ transform: translateX(-50%); }}
        }}
        </style>

        <div class="slider">
            <div class="track">
                {imgs_html}
            </div>
        </div>
        """

        components.html(html_code, height=250)

        st.markdown("---")

        # =====================================================
        # 2️⃣ SIMPLE SLIDESHOW (SAFE STREAMLIT VERSION)
        # =====================================================
        st.markdown("### 🔄 Auto Slideshow")

        if "mem_i" not in st.session_state:
            st.session_state.mem_i = 0

        col1, col2, col3 = st.columns([1,2,1])

        with col2:
            st.image(images[st.session_state.mem_i], width=600)

        if st.button("Next Memory ➡️"):
            st.session_state.mem_i = (st.session_state.mem_i + 1) % len(images)

        if st.button("⬅️ Previous"):
            st.session_state.mem_i = (st.session_state.mem_i - 1) % len(images)

        st.markdown("---")

        # =====================================================
        # 3️⃣ FLOATING GALLERY
        # =====================================================
        st.markdown("### 🌊 Floating Gallery")

        cols = st.columns(3)

        for i, img in enumerate(images):
            with cols[i % 3]:
                st.image(img, use_container_width=True)

        st.markdown("---")

        # =====================================================
        # 4️⃣ VIEWER
        # =====================================================
        st.markdown("### 🔍 Memory Viewer")

        selected = st.selectbox("Select Memory 💖", images)
        st.image(selected, width=650)
        # =========================================================
# TAB 5 - CELEBRATION (FINAL BIRTHDAY EFFECTS)
# =========================================================
with tab5:

    st.markdown("""
    <style>
    /* BIG TITLE */
    .big-title {
        text-align:center;
        font-size:85px;
        color:#ff2e63;
        font-weight:900;
        text-shadow:0 0 50px #ff2e63;
        animation: glow 2s infinite alternate;
    }

    @keyframes glow {
        from {transform: scale(1);}
        to {transform: scale(1.05);}
    }

    /* INFO BOX */
    .box {
        background: rgba(255,255,255,0.06);
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------------- TITLE ----------------
    st.markdown("<div class='big-title'>🎉 HAPPY BIRTHDAY TO YOU 🎉</div>", unsafe_allow_html=True)

    

    # ---------------- MUSIC ----------------
    st.markdown("## 🎵 Birthday Song")

    try:
        audio_path = os.path.join(BASE, "song.mp3")
        audio_file = open(audio_path, "rb")
        st.audio(audio_file.read(), format="audio/mp3")
    except:
        st.warning(" Please add song.mp3 in your project folder")

    # ---------------- FIREWORKS EFFECT ----------------
    components.html("""
    <html>
    <body style="margin:0;overflow:hidden;background:transparent;">

    <script>
    for(let i=0;i<80;i++){
        let d=document.createElement("div");
        d.style.position="absolute";
        d.style.left=Math.random()*100+"%";
        d.style.top=Math.random()*100+"%";
        d.style.width="6px";
        d.style.height="6px";
        d.style.background=["red","pink","yellow","cyan","white"][Math.floor(Math.random()*5)];
        d.style.borderRadius="50%";
        d.style.animation="boom 2s infinite";
        document.body.appendChild(d);
    }
    </script>

    <style>
    @keyframes boom {
        0% {transform: scale(0); opacity: 1;}
        100% {transform: scale(12); opacity: 0;}
    }
    </style>

    </body>
    </html>
    """, height=450)

    # ---------------- FINAL EFFECTS ----------------
    st.balloons()
    st.snow()

    st.success("🎂 Happy Birthday DEAR 🎉💖")
