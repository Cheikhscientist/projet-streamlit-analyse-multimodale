import streamlit as st
from csv_analysis import csv_page
from text_analysis import text_page
from image_analysis import image_page

st.set_page_config(page_title="Analyse Multimodale", layout="wide")
st.title("Application d’analyse multimodale")

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

