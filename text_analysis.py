import re
from collections import Counter
from nltk.corpus import stopwords
from textblob import TextBlob

def clean_text(text):
    """
    Nettoie un texte :
    - minuscules
    - suppression ponctuation
    - suppression stopwords
    """
    text = text.lower()
    text = re.sub(r"[^a-zA-ZÀ-ÿ\s]", "", text)

    stop_words = set(stopwords.words("french"))
    words = [w for w in text.split() if w not in stop_words]

    return " ".join(words)


def text_statistics(text):
    """
    Retourne :
    - nombre de mots
    - longueur du texte
    - mots les plus fréquents
    """
    words = text.split()
    return {
        "word_count": len(words),
        "char_count": len(text),
        "top_words": Counter(words).most_common(10)
    }


def sentiment_analysis(text):
    """
    Analyse de sentiment simple via TextBlob.
    Retourne polarité et subjectivité.
    """
    blob = TextBlob(text)
    return {
        "polarity": blob.sentiment.polarity,
        "subjectivity": blob.sentiment.subjectivity
    }

