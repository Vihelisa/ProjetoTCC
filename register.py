import streamlit as st
from PIL import Image
from auth import login, register
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


def register_page():
    image = Image.open("title.png")

    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{image_to_base64(image)}" width="350">
        </div>
        """,unsafe_allow_html=True)

    st.title("Cadastro")
    username = st.text_input("Novo usuário")
    password = st.text_input("Nova senha", type="password")
    if st.button("Registrar"):
        if register(username, password):
            st.toast("Cadastro realizado com sucesso!", icon="✅")
            go_to_login()
        else:
            st.toast("Usuário já existe.", icon="❌")
    if st.button("Voltar"):
        go_to_login()
