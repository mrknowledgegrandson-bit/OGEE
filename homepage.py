import streamlit as st
import base64

# ---------------- PAGE CONFIG (TOUJOURS EN PREMIER) ----------------
st.set_page_config(
    page_title="OG££ FR££D0 - Officiel",
    page_icon="🔥",
    layout="centered"
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
            filter: blur(1px); /* fond légèrement flouté */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Définir l'image de fond (mettre le fichier dans le même dossier que ce script)
set_bg("og2.jpg")

# ------------------- STYLE SUPPLÉMENTAIRE -------------------
st.markdown(
    """
    <style>
    /* Couleur et style du texte sur le fond */
    h1, h2, h3, p {
        text-align: center;
        color: white;
        font-family: 'Arial', sans-serif;
    }

    /* Icônes réseaux : effet au survol */
    .social-icon img {
        transition: transform 0.3s;
    }
    .social-icon img:hover {
        transform: scale(1.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
    <p style='color:white; font-size:18px;'>
    Je suis un jeune créateur de contenu passionné par la géopolitique et la technologie dans le monde et en Afrique.<br><br>
    Passionné du continent africain et de son développement.<br><br>
    Mon objectif est d’informer, d’inspirer, d’éduquer et de construire une grande communauté consciente africaine.<br><br>
    Je veux ouvrir les yeux de la jeunesse africaine 
    </p>
    """,
    unsafe_allow_html=True
)
st.divider()

# ------------------- LIENS RÉSEAUX -------------------
st.markdown("<h2>🌍 Rejoins-moi ici</h2>", unsafe_allow_html=True)

youtube = "https://www.youtube.com/@MRKNOWLEDGE-o4m"
tiktok = "https://www.tiktok.com/@og_malien"
instagram = "https://www.instagram.com/poloniumboy210/"

st.markdown(
    f"""
    <div style="display:flex;justify-content:center;gap:40px;">
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
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ------------------- PIED DE PAGE -------------------
st.markdown("<p>© 2026 - OG££ FR££D0 | Tous droits réservés</p>", unsafe_allow_html=True)
