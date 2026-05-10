import streamlit as st
import base64

# ---------------- PAGE CONFIG (TOUJOURS EN PREMIER) ----------------
st.set_page_config(
    page_title="OG££ FR££D0 - Officiel",
    page_icon="og3.png",  # logo local
    layout="centered"
)

# ------------------- LIENS RÉSEAUX -------------------
youtube = "https://www.youtube.com/@MRKNOWLEDGE-o4m"
tiktok = "https://www.tiktok.com/@og_malien"
instagram = "https://www.instagram.com/poloniumboy210/"
twitter = ""

# ------------------- BARRE RÉSEAUX EN HAUT À DROITE -------------------
st.markdown(
    f"""
    <style>
    .top-social {{
        position: fixed;
        top: 15px;
        right: 20px;
        display: flex;
        align-items: center;
        gap: 12px;
        z-index: 9999;
        background: rgba(0,0,0,0.45);
        padding: 8px 14px;
        border-radius: 20px;
        backdrop-filter: blur(4px);
    }}
    .top-social span {{
        color: white;
        font-size: 14px;
        margin-right: 6px;
    }}
    .top-social img {{
        width: 26px;
        transition: transform 0.3s;
    }}
    .top-social img:hover {{
        transform: scale(1.2);
    }}

    /* Styles globaux */
    h1, h2, h3, p {{
        text-align: center;
        color: white;
        font-family: Arial, sans-serif;
    }}
    .social-icon img {{
        transition: transform 0.3s;
    }}
    .social-icon img:hover {{
        transform: scale(1.2);
    }}

    /* Logo X en SVG (officiel) */
    .x-link {{
        width: 26px;
        height: 26px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
    }}
    .x-link.big {{
        width: 60px;
        height: 60px;
    }}
    .x-svg {{
        width: 100%;
        height: 100%;
        fill: white;
        transition: transform 0.3s;
    }}
    .x-link:hover .x-svg {{
        transform: scale(1.2);
    }}
    </style>

    <div class="top-social">
        <span>👉 Cliquez</span>
        <a href="{youtube}" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/1384/1384060.png">
        </a>
        <a href="{tiktok}" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/3046/3046121.png">
        </a>
        <a href="{instagram}" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/1384/1384063.png">
        </a>
        <a href="{twitter}" target="_blank" class="x-link">
            <svg class="x-svg" viewBox="0 0 1200 1227" xmlns="http://www.w3.org/2000/svg">
                <path d="M714.163 519.284L1160.89 0H1055.03L667.137 450.887L357.328 0H0L468.492 681.821L0 1226.37H105.866L515.491 750.218L842.672 1226.37H1200L714.137 519.284H714.163ZM569.165 687.828L521.797 619.934L144.011 79.6944H306.615L611.412 515.685L658.78 583.579L1055.08 1146.68H892.476L569.165 687.854V687.828Z"/>
            </svg>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# --------- FONCTION POUR LE BACKGROUND ---------
def set_bg(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Image de fond
set_bg("og2.jpg")

# ------------------- HEADER -------------------
st.image("og.jpg", use_container_width=True)

st.markdown("<h1>🔥 OG££ FR££D0</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color:#ff4444;'>Créateur de contenu éducatif | Géopolitique | Visionnaire</h3>", unsafe_allow_html=True)
st.markdown("<p>Bienvenue sur mon site officiel.<br>Ici, tu peux me découvrir et rejoindre ma communauté.</p>", unsafe_allow_html=True)
st.divider()

# ------------------- À PROPOS -------------------
st.markdown("<h2>👤 À propos de moi</h2>", unsafe_allow_html=True)
st.markdown(
    """
    <p style='font-size:18px;'>
    Je suis un jeune créateur de contenu passionné par la géopolitique et la technologie dans le monde et en Afrique.<br><br>
    Passionné du continent africain et de son développement.<br><br>
    Mon objectif est d’informer, d’inspirer, d’éduquer et de construire une grande communauté consciente africaine.<br><br>
    
    </p>
    """,
    unsafe_allow_html=True
)
st.divider()

# ------------------- LIENS RÉSEAUX (BAS DE PAGE) -------------------
st.markdown("<h2>🌍 Rejoins-moi ici</h2>", unsafe_allow_html=True)

st.markdown(
    f"""
    <div style="display:flex;justify-content:center;gap:40px;align-items:center;">
        <div class="social-icon">
            <a href="{youtube}" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/1384/1384060.png" width="60">
            </a>
        </div>
        <div class="social-icon">
            <a href="{tiktok}" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/3046/3046121.png" width="60">
            </a>
        </div>
        <div class="social-icon">
            <a href="{instagram}" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/1384/1384063.png" width="60">
            </a>
        </div>
        <a href="{twitter}" target="_blank" class="x-link big">
            <svg class="x-svg" viewBox="0 0 1200 1227" xmlns="http://www.w3.org/2000/svg">
                <path d="M714.163 519.284L1160.89 0H1055.03L667.137 450.887L357.328 0H0L468.492 681.821L0 1226.37H105.866L515.491 750.218L842.672 1226.37H1200L714.137 519.284H714.163ZM569.165 687.828L521.797 619.934L144.011 79.6944H306.615L611.412 515.685L658.78 583.579L1055.08 1146.68H892.476L569.165 687.854V687.828Z"/>
            </svg>
        </a>
    </div>
    <p style="margin-top:10px;">👉 Cliquez sur une icône pour me rejoindre</p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ------------------- PIED DE PAGE -------------------
st.markdown("<p>© 2026 - OG££ FR££D0 | Tous droits réservés</p>", unsafe_allow_html=True)


