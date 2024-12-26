import streamlit as st
import pandas as pd
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# # Charger les données des comptes depuis le fichier CSV
users = pd.read_csv('users.csv', sep=',')


def charger_donnees_utilisateurs(fichier_csv):
    df = pd.read_csv(fichier_csv, sep=',')
    # Conversion en dictionnaire au format attendu par streamlit-authenticator
    users_data = {'usernames': {}}
    for _, row in df.iterrows():
        users_data['usernames'][row['name']] = {
            'name': row['name'],
            'password': row['password'],
            'email': row['email']
        }

    return users_data

# Chemin vers le fichier CSV
fichier_csv = "users.csv"  # Assure-toi que ce fichier existe dans le répertoire courant
users = charger_donnees_utilisateurs(fichier_csv)

authenticator = Authenticate(
    credentials=users,        # Les données des comptes
    cookie_name="cookie_name", # Le nom du cookie
    key="cookie_key",          # La clé du cookie
    cookie_expiry_days=30      # Nombre de jours avant expiration
)

authenticator.login()

def accueil():
    st.title("Bienvenu sur ma page")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSq9XYKLl7Qr8OxmMWJZ2TJE7famhvHD_yTyg&s",width=700)
    st.write("Bienvenue sur la page d'accueil !")

def photos():
    st.title("Bienvenue sur mon album photo")
    st.write("S'il fallait que j'aie un animal, il serait un husky...")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.write("... aux yeux doux")
        st.image("https://previews.123rf.com/images/filipstudio/filipstudio1707/filipstudio170700022/83726041-le-chien-husky-vient-magnifiquement-avec-des-yeux-diff%C3%A9rentes-%C3%A0-la-maison.jpg")
    with col2:
        st.write("... boudeur")
        st.image("https://cdn.playgrnd.media/v7/img/ph/usr_a6bbebef-98d0-40ee-a709-46236788bc0c/chd_bc1359a1-62b8-43d8-9663-f3586bf30e65/ph_6fd0ef21-8eab-40f2-8f12-c8ffa7514554.jpg?align=32,21&w=1080&h=1080&q=45")
    with col3:
        st.write("... BFF")
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT12DcXFzNxOIkKubOVuDV0qSeJC2QmOt143A&s")
    with col4:
        st.write("... à problème")
        st.image("https://preview.redd.it/dep5y51uvic41.jpg?width=1080&crop=smart&auto=webp&s=8a4d4a62b4669072eeb43934e7ffedd1690d0409")
    with col5:
        st.write("... à grimaces bizarres")
        st.image("https://preview.redd.it/rescued-this-pretty-girl-off-the-streets-what-kind-of-husky-v0-t4yfunju5mdd1.jpg?width=989&format=pjpg&auto=webp&s=20516fa2a99fe66c969d83d4588978dab9bc3b7f")

if st.session_state["authentication_status"]:
    with st.sidebar:
        name = st.session_state['name']
        authenticator.logout("Déconnexion")
        st.write(f"Bienvenue {name}")
        # Création du menu qui va afficher les choix qui se trouvent dans la variable options
        selection = option_menu(
                menu_title=None,
                options = ["Accueil", "Photos"]
            )

# On indique au programme quoi faire en fonction du choix
    if selection == "Accueil":
        accueil()
    elif selection == "Photos":
        photos()

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')