import streamlit as st
from PIL import Image, ImageOps, ImageFilter

def image_page():
    st.header("🖼️ Analyse et traitement d’images")

    st.markdown(
        "Importez une image, explorez ses métadonnées et appliquez "
        "des transformations et effets visuels."
    )

    st.divider()

    # Upload image
    file = st.file_uploader(
        "📂 Importer une image",
        type=["jpg", "jpeg", "png"]
    )

    if file is None:
        st.info("Veuillez importer une image pour commencer.")
        return

    image = Image.open(file)

    # Métadonnées
    st.subheader("📋 Métadonnées")
    col_meta1, col_meta2 = st.columns(2)

    with col_meta1:
        st.write(f"**Nom :** {file.name}")
        st.write(f"**Format :** {image.format}")
    with col_meta2:
        st.write(f"**Dimensions :** {image.size[0]} x {image.size[1]} px")
        st.write(f"**Mode couleur :** {image.mode}")

    # Image originale
    st.subheader("🖼️ Image originale")
    st.image(image, use_container_width=True)

    # Paramètres
    st.subheader("⚙️ Transformations de base")
    col1, col2, col3 = st.columns(3)

    with col1:
        grayscale = st.checkbox("Niveaux de gris")

    with col2:
        rotate = st.slider("Rotation (°)", -180, 180, 0)

    with col3:
        resize = st.slider("Redimensionnement max (px)", 100, 2000, 500)

    # Effets visuels
    st.subheader("🎨 Effets visuels")
    effect = st.selectbox(
        "Choisir un effet",
        ["Aucun", "Contours", "Cartoon", "Inversion des couleurs"]
    )

    # Application des transformations
    processed = image.copy()

    if grayscale:
        processed = ImageOps.grayscale(processed)

    processed.thumbnail((resize, resize))

    if rotate != 0:
        processed = processed.rotate(rotate, expand=True)

    # Application des effets
    if effect == "Contours":
        processed = ImageOps.grayscale(processed).filter(ImageFilter.FIND_EDGES)

    elif effect == "Cartoon":
        edges = ImageOps.grayscale(processed).filter(ImageFilter.FIND_EDGES)
        processed = ImageOps.colorize(edges, black="black", white="white")

    elif effect == "Inversion des couleurs":
        processed = ImageOps.invert(processed.convert("RGB"))

    # Comparaison avant / après
    st.subheader("🔍 Comparaison avant / après")
    colA, colB = st.columns(2)

    with colA:
        st.image(image, caption="Originale", use_container_width=True)

    with colB:
        st.image(processed, caption="Après traitement", use_container_width=True)

    # Dimensions finales
    st.caption(
        f"📐 Dimensions originales : {image.size[0]} x {image.size[1]} px | "
        f"Après traitement : {processed.size[0]} x {processed.size[1]} px"
    )
