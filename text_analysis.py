import streamlit as st
import re
from collections import Counter
from textblob import TextBlob
import nltk

# Assure-toi que les stopwords sont bien téléchargés
nltk.download('stopwords')
from nltk.corpus import stopwords

def page_text():
    st.title("📝 Analyse de texte")

    uploaded_file = st.file_uploader("Importer un fichier texte (.txt)", type=["txt"])
    raw_text = ""

    if uploaded_file is not None:
        raw_text = uploaded_file.read().decode("utf-8")
    else:
        raw_text = st.text_area("Ou collez votre texte ici", height=200)

    if raw_text:
        st.subheader("🔧 Nettoyage du texte")

        def clean_text(text):
            text = text.lower()
            text = re.sub(r"[^a-zA-ZÀ-ÿ\s]", "", text)
            stop_words = set(stopwords.words("french"))
            words = [w for w in text.split() if w not in stop_words]
            return " ".join(words)

        cleaned = clean_text(raw_text)
        st.text_area("Texte nettoyé", cleaned, height=200)

        st.subheader("📊 Statistiques textuelles")

        words = cleaned.split()
        word_count = len(words)
        char_count = len(cleaned)
        top_words = Counter(words).most_common(10)

        st.write(f"**Nombre de mots :** {word_count}")
        st.write(f"**Nombre de caractères :** {char_count}")
        st.write("**Mots les plus fréquents :**")
        st.table(top_words)

        st.subheader("💬 Analyse de sentiment")

        blob = TextBlob(cleaned)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        st.write(f"**Polarité :** {polarity:.2f}")
        st.write(f"**Subjectivité :** {subjectivity:.2f}")


