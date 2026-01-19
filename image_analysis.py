import streamlit as st
from PIL import Image, ImageOps
import io

def image_page():
    st.title("🖼️ Analyse et Traitement d'Images")
    st.write("Appliquez plusieurs transformations simultanément et comparez les résultats.")

    # Import de l'image
    uploaded_file = st.file_uploader("Choisissez une image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # 1. Chargement de l'originale
        original_img = Image.open(uploaded_file)
        
        # --- BARRE LATÉRALE POUR LES MODIFICATIONS ---
        st.sidebar.header("⚙️ Paramètres de modification")
        
        # Option Niveaux de gris
        apply_grayscale = st.sidebar.checkbox("Niveaux de gris")
        
        # Option Rotation
        angle = st.sidebar.slider("Rotation (degrés)", 0, 360, 0)
        
        # Option Redimensionnement
        scale = st.sidebar.slider("Redimensionnement (%)", 10, 200, 100)
        
        # Option Inversion des couleurs (bonus TP)
        apply_invert = st.sidebar.checkbox("Inverser les couleurs")

        # --- TRAITEMENT DE L'IMAGE (Accumulation des modifs) ---
        # On part d'une copie pour appliquer les filtres un par un
        modified_img = original_img.copy()

        if apply_grayscale:
            modified_img = ImageOps.grayscale(modified_img)
            # On convertit en RGB pour garder la compatibilité avec les autres filtres si besoin
            modified_img = modified_img.convert("RGB")
            
        if apply_invert:
            # L'inversion nécessite du RGB (pas de RGBA)
            if modified_img.mode == 'RGBA':
                modified_img = modified_img.convert("RGB")
            modified_img = ImageOps.invert(modified_img)

        if angle != 0:
            modified_img = modified_img.rotate(angle, expand=True)

        if scale != 100:
            new_w = int(modified_img.width * scale / 100)
            new_h = int(modified_img.height * scale / 100)
            modified_img = modified_img.resize((new_w, new_h))

        # --- AFFICHAGE CÔTE À CÔTE ---
        st.subheader("🔍 Comparaison avant / après")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Originale**")
            st.image(original_img, use_container_width=True)
            
            # Affichage des métadonnées sous l'originale
            with st.expander("Voir les métadonnées"):
                st.write(f"Format: {original_img.format}")
                st.write(f"Taille: {original_img.size}")
                st.write(f"Mode: {original_img.mode}")

        with col2:
            st.markdown("**Modifiée**")
            st.image(modified_img, use_container_width=True)
            
            # Bouton de téléchargement pour l'image finale
            buf = io.BytesIO()
            # On sauvegarde en PNG pour préserver la qualité des modifs
            modified_img.save(buf, format="PNG")
            st.download_button(
                label="💾 Télécharger l'image modifiée",
                data=buf.getvalue(),
                file_name="image_traitee.png",
                mime="image/png"
            )

# Lancement
if __name__ == "__main__":
    image_page()
