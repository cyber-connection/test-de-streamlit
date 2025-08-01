import streamlit as st

st.title("👋 Bienvenue dans mon interface Streamlit")

nom = st.text_input("Entrez votre nom")

if st.button("Dire bonjour"):
    st.success(f"Bonjour {nom} ! Ravie de te voir ici.")
