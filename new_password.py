import streamlit as st
from PIL import Image
from config.auth import login, register
from io import BytesIO
import base64

from functions.functions import *

def go_to_login():
    st.session_state.page = "login"

def go_to_register():
    st.session_state.page = "register"

def go_to_home():
    st.session_state.page = "home"
    st.session_state.logged_in = True



def password_page():
    image = Image.open("title.png")

    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{image_to_base64(image)}" width="350">
        </div>
        """,unsafe_allow_html=True)


    st.title("Nova Senha")
    email = st.text_input("Digite seu email:")
    new_password = st.text_input("Digite sua nova senha:")
    password = st.text_input("Confirme nova senha:", type="password")
    if st.button("Registrar"):
        if new_password != password:
            st.toast("As senhas não coincidem.", icon="❌")
        else:
            if register_new_password(email, new_password):
                st.toast("Cadastro realizado com sucesso!", icon="✅")
                go_to_login()
            else:
                st.toast("Erro ao cadastrar nova senha.", icon="❌")
    if st.button("Voltar"):
        go_to_login()
