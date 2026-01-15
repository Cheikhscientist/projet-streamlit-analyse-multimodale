#  Analyse Multimodale avec Streamlit

Application d’analyse **CSV**, **texte** et **images** développée en Python avec Streamlit.

## Accès à l’application
L’application est accessible en ligne à l’adresse :
[https://TON-LIEN.streamlit.app](https://projet-app-analyse-multimodale-c9xyt7rdxexmisnvx8f3rf.streamlit.app/)

---

##  Présentation du projet

Cette application Streamlit permet d’explorer et d’analyser trois types de données :

- **Données tabulaires (CSV)**
- **Données textuelles (texte brut ou fichiers .txt)**
- **Données visuelles (images .jpg/.png)**

Elle illustre :

- Une architecture Python propre et modulaire  
- L’utilisation de bibliothèques modernes (Pandas, PIL, TextBlob, Seaborn…)  
- Une interface utilisateur simple et interactive grâce à Streamlit  

---

##  Fonctionnalités

###  1. Analyse de fichiers CSV
- Importation de fichiers CSV  
- Validation des données :  
  - valeurs manquantes  
  - doublons  
  - types des colonnes  
- Statistiques descriptives  
- Visualisations :  
  - histogrammes  
  - boxplots  
  - matrice de corrélation  
- Filtres interactifs :  
  - numériques (sliders)  
  - catégoriels (selectbox)  
  - dates  

---

###  2. Analyse de texte
- Importation de texte brut ou fichiers `.txt`  
- Nettoyage automatique :  
  - minuscules  
  - suppression ponctuation  
  - suppression stopwords  
- Statistiques textuelles :  
  - nombre de mots  
  - longueur du texte  
  - mots les plus fréquents  
- Analyse de sentiment (TextBlob)

---

###  3. Analyse d’images
- Importation d’images `.jpg` / `.png`  
- Affichage et extraction des métadonnées EXIF  
- Transformations :  
  - conversion en niveaux de gris  
  - redimensionnement  
  - rotation  

---



