import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def csv_page():
    st.header("Analyse de fichiers CSV")

    # =========================
    # 1. Import du fichier CSV
    # =========================
    file = st.file_uploader("Importer un fichier CSV", type=["csv"])

    if file is None:
        st.info("Veuillez importer un fichier CSV.")
        return

    df = pd.read_csv(file)

    st.subheader("Aperçu des données")
    st.dataframe(df)

    # =========================
    # 2. Validation des données
    # =========================
    st.subheader("Validation des données")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("Valeurs manquantes")
        st.write(df.isnull().sum())

    with col2:
        st.write("Nombre de doublons")
        st.write(df.duplicated().sum())

    with col3:
        st.write("Types de colonnes")
        st.write(df.dtypes)

    # =========================
    # 3. Filtres interactifs
    # =========================
    st.subheader("Filtres interactifs")

    filtered_df = df.copy()

    # --- Filtre catégoriel ---
    cat_cols = filtered_df.select_dtypes(include=["object"]).columns
    if len(cat_cols) > 0:
        cat_col = st.selectbox("Filtrer par colonne catégorielle", cat_cols)
        cat_values = st.multiselect(
            "Valeurs à conserver",
            filtered_df[cat_col].unique(),
            default=list(filtered_df[cat_col].unique())
        )
        filtered_df = filtered_df[filtered_df[cat_col].isin(cat_values)]

    # --- Filtre numérique ---
    num_cols = filtered_df.select_dtypes(include=["int64", "float64"]).columns
    if len(num_cols) > 0:
        num_col = st.selectbox("Filtrer par colonne numérique", num_cols)

        min_val = float(filtered_df[num_col].min())
        max_val = float(filtered_df[num_col].max())

        selected_range = st.slider(
            f"Plage de valeurs pour {num_col}",
            min_val,
            max_val,
            (min_val, max_val)
        )

        filtered_df = filtered_df[
            (filtered_df[num_col] >= selected_range[0]) &
            (filtered_df[num_col] <= selected_range[1])
        ]

    st.subheader("Données après filtres")
    st.dataframe(filtered_df)

    # =========================
    # 4. Statistiques descriptives
    # =========================
    st.subheader("Statistiques descriptives")
    st.write(filtered_df.describe())

    # =========================
    # 5. Visualisations
    # =========================
    st.subheader("Visualisations")

    numeric_cols = filtered_df.select_dtypes(include=["int64", "float64"]).columns

    if len(numeric_cols) == 0:
        st.warning("Aucune colonne numérique disponible pour les visualisations.")
        return

    col = st.selectbox("Choisir une colonne numérique", numeric_cols)

    # --- Histogramme ---
    st.markdown("### Histogramme")
    fig1, ax1 = plt.subplots()
    ax1.hist(filtered_df[col].dropna(), bins=20)
    ax1.set_title(f"Histogramme de {col}")
    st.pyplot(fig1)

    # --- Boxplot ---
    st.markdown("### Boxplot")
    fig2, ax2 = plt.subplots()
    ax2.boxplot(filtered_df[col].dropna(), vert=False)
    ax2.set_title(f"Boxplot de {col}")
    st.pyplot(fig2)

    # --- Corrélation ---
    st.markdown("### Matrice de corrélation")

    if len(numeric_cols) > 1:
        corr = filtered_df[numeric_cols].corr()
        fig3, ax3 = plt.subplots()
        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax3)
        st.pyplot(fig3)
    else:
        st.info("Pas assez de colonnes numériques pour calculer une corrélation.")
