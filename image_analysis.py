
import streamlit as st
from PIL import Image, ImageOps

def image_page():
    st.header("Analyse et traitement d’images")

    # Upload image
    file = st.file_uploader(
        "Importer une image",
        type=["jpg", "jpeg", "png"]
    )

    if file is None:
        st.info("Veuillez importer une image")
        return

    # Chargement image
    image = Image.open(file)

    # Métadonnées
    st.subheader("Métadonnées")
    st.write(f"Nom du fichier : {file.name}")
    st.write(f"Format : {image.format}")
    st.write(f"Dimensions : {image.size[0]} x {image.size[1]} px")
    st.write(f"Mode couleur : {image.mode}")

    # Affichage image originale
    st.subheader("Image originale")
    st.image(image, caption="Image originale", use_container_width=True)

    # Paramètres de transformation
    st.subheader("Transformations")

    col1, col2, col3 = st.columns(3)

    with col1:
        grayscale = st.checkbox("Niveaux de gris")

    with col2:
        rotate = st.slider("Rotation (degrés)", -180, 180, 0)

    with col3:
        resize = st.slider("Redimensionnement max (px)", 100, 2000, 500)

    # Application transformations
    processed = image.copy()

    if grayscale:
        processed = ImageOps.grayscale(processed)

    processed.thumbnail((resize, resize))

    if rotate != 0:
        processed = processed.rotate(rotate, expand=True)

    # Affichage image transformée
    st.subheader("Image transformée")
    st.image(processed, caption="Image après transformation", use_container_width=True)
