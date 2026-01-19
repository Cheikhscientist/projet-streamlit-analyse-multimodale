import streamlit as st
from PIL import Image, ImageOps
import io

def image_page():
    """
    Fonction gérant la section 'Analyse d'images' du projet.
    Inclut l'importation, l'affichage des métadonnées et les transformations.
    """
    st.title("🖼️ Analyse d'Images")
    st.write("Importez une image pour l'analyser et l'éditer.")

    # 1. Import d'images (jpg, png) - Contrainte technique du projet 
    uploaded_file = st.file_uploader("Choisissez une image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Chargement de l'image avec Pillow 
        image = Image.open(uploaded_file)
        
        # Mise en page avec colonnes
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Aperçu")
            st.image(image, use_container_width=True)

        with col2:
            # 2. Affichage des métadonnées (Taille et Mode) 
            st.subheader("Métadonnées")
            st.write(f"**Format :** {image.format}")
            st.write(f"**Dimensions :** {image.size[0]} x {image.size[1]} pixels")
            st.write(f"**Mode de couleur :** {image.mode}")

        st.divider()

        # 3. Transformations basiques 
        st.subheader("🛠️ Transformations")
        
        transformation = st.selectbox(
            "Sélectionnez une action :",
            ["Conserver l'original", "Niveaux de gris", "Redimensionner", "Pivoter"]
        )

        # On travaille sur une copie pour ne pas modifier l'originale
        img_modified = image.copy()

        if transformation == "Niveaux de gris":
            img_modified = ImageOps.grayscale(img_modified)
            st.image(img_modified, caption="Version noir et blanc")

        elif transformation == "Redimensionner":
            ratio = st.slider("Ratio de taille (%)", 10, 200, 100)
            new_w = int(image.width * ratio / 100)
            new_h = int(image.height * ratio / 100)
            img_modified = img_modified.resize((new_w, new_h))
            st.image(img_modified, caption=f"Redimensionné en : {new_w}x{new_h}")

        elif transformation == "Pivoter":
            angle = st.slider("Angle (degrés)", 0, 360, 0)
            img_modified = img_modified.rotate(angle)
            st.image(img_modified, caption=f"Rotation de {angle}°")

        # Option de téléchargement pour l'image transformée
        if transformation != "Conserver l'original":
            buf = io.BytesIO()
            img_modified.save(buf, format="PNG")
            st.download_button(
                label="💾 Télécharger l'image modifiée",
                data=buf.getvalue(),
                file_name="image_analyse.png",
                mime="image/png"
            )

# Exemple d'appel dans le fichier principal
if __name__ == "__main__":
    image_page()
