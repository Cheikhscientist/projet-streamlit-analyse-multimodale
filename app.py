import streamlit as st
from csv_analysis import csv_page
from text_analysis import text_page
from image_analysis import image_page

st.set_page_config(
    page_title="Analyse multimodale",
    layout="wide",
    page_icon="📊"
)

st.title("📊 Application d’analyse multimodale")

st.markdown(
    """
    Cette application permet d’analyser :
    - 📁 des fichiers CSV  
    - 📝 des textes  
    - 🖼️ des images  

    Sélectionnez un type d’analyse dans le menu à gauche.
    """
)

st.divider()


menu = st.sidebar.selectbox(
    "Choisir une analyse",
    ["CSV", "Texte", "Image"]
)

if menu == "CSV":
    csv_page()
elif menu == "Texte":
    text_page()
elif menu == "Image":
    image_page()

