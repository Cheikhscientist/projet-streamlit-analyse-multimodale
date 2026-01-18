import streamlit as st
import re
from collections import Counter
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords

# Téléchargement sécurisé des stopwords (une seule fois)
try:
    stopwords.words("french")
except LookupError:
    nltk.download("stopwords")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-ZÀ-ÿ\s]", "", text)
    stop_words = set(stopwords.words("french"))
    words = [w for w in text.split() if w not in stop_words]
    return " ".join(words)

def text_page():
    st.header("📝 Analyse de texte")

    st.markdown(
        "Analyse d’un texte brut ou d’un fichier `.txt` : "
        "nettoyage, statistiques simples et analyse de sentiment."
    )

    st.divider()

    uploaded_file = st.file_uploader("📂 Importer un fichier texte (.txt)", type=["txt"])

    raw_text = ""
    if uploaded_file:
        raw_text = uploaded_file.read().decode("utf-8")
    else:
        raw_text = st.text_area(
            "✏️ Ou collez votre texte ici",
            height=200,
            placeholder="Exemple : This project is amazing but challenging..."
        )

    if not raw_text:
        st.info("Veuillez saisir ou importer un texte pour commencer.")
        return

    # Nettoyage
    st.subheader("🔧 Nettoyage du texte")
    cleaned = clean_text(raw_text)

    with st.expander("Afficher le texte nettoyé"):
        st.write(cleaned)

    # Statistiques
    st.subheader("📊 Statistiques textuelles")
    words = cleaned.split()

    col1, col2, col3 = st.columns(3)
    col1.metric("Nombre de mots", len(words))
    col2.metric("Nombre de caractères", len(cleaned))
    col3.metric("Mots uniques", len(set(words)))

    st.subheader("🔁 Mots les plus fréquents")
    top_words = Counter(words).most_common(10)
    st.table(top_words)

    # Sentiment
    st.subheader("💬 Analyse de sentiment")
    blob = TextBlob(raw_text)

    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0.1:
        st.success(f"Sentiment global : POSITIF ({polarity:.2f}) 😊")
    elif polarity < -0.1:
        st.error(f"Sentiment global : NÉGATIF ({polarity:.2f}) 😡")
    else:
        st.warning(f"Sentiment global : NEUTRE ({polarity:.2f}) 😐")

    st.caption(
        f"Subjectivité : {subjectivity:.2f} — "
        "Analyse de sentiment simple basée sur TextBlob (indicative)."
    )
