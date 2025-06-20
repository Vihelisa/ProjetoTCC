import streamlit as st
from PIL import Image
from config.auth import login, register
from io import BytesIO
import base64
import re

from functions.functions import *

def go_to_login():
    st.session_state.page = "login"

def go_to_register():
    st.session_state.page = "register"

def go_to_home():
    st.session_state.page = "home"
    st.session_state.logged_in = True


def register_page():
    image = Image.open("title.png")

    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{image_to_base64(image)}" width="350">
        </div>
        """,unsafe_allow_html=True)

    st.title("Cadastro")
    name = st.text_input("Nome:")
    num_oab = st.text_input("Número OAB:")
    email = st.text_input("Digite um email válido:")
    conf_email = st.text_input("Confirme o email:", key="conf_email")
    password = st.text_input("Senha de acesso:", type="password")
    username = email.split('@')[0]
    username_bd = username = re.sub(r'[^a-zA-Z0-9]', '', username)
    if st.button("Cadastrar"):
        if email == conf_email:
            register_dict = {
                'nome': name,
                'email': email,
                'senha': password,
                'num_oab': num_oab,
                'username': username_bd
            }

            register_bd_dict = {
                'username': username_bd,
                'password': username_bd
            }

            if register(register_dict, register_bd_dict) == True:
                st.toast("Cadastro realizado com sucesso!", icon="✅")
                go_to_login()
            else: st.toast("Usuário já existe.", icon="❌")
        else: st.toast("Os emails não coincidem.", icon="❌")
    if st.button("Voltar"):
        go_to_login()
