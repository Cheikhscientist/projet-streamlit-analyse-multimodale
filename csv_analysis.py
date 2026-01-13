import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def csv_page():
    st.header("Analyse de fichiers CSV")

    file = st.file_uploader("Importer un fichier CSV", type=["csv"])

    if file is None:
        st.info("Veuillez importer un fichier CSV")
        return

    df = pd.read_csv(file)
    st.subheader("Aperçu des données")
    st.dataframe(df)

    # Validation
    st.subheader("Validation des données")
    st.write("Valeurs manquantes par colonne :")
    st.write(df.isnull().sum())

    st.write(f"Nombre de doublons : {df.duplicated().sum()}")

    # Statistiques
    st.subheader("Statistiques descriptives")
    st.write(df.describe())

    # Visualisation
    st.subheader("Visualisation")

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    if len(numeric_cols) > 0:
        col = st.selectbox("Choisir une colonne numérique", numeric_cols)
        fig, ax = plt.subplots()
        ax.hist(df[col].dropna())
        ax.set_title(f"Histogramme de {col}")
        st.pyplot(fig)
    else:
        st.warning("Aucune colonne numérique détectée")

