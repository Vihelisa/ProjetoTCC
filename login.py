import streamlit as st
from PIL import Image
from auth import login, register
from io import BytesIO
import base64

from functions.functions import *


def go_to_home():
    st.session_state.page = "home"
    st.session_state.logged_in = True

def go_to_register():
    st.session_state.page = "register"

def go_to_new_password():
    st.session_state.page = "password"



def login_page():    
    image = Image.open("title.png")

    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{image_to_base64(image)}" width="350">
        </div>
        """,unsafe_allow_html=True)

    st.title("Login")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")

    
    # Criar duas colunas para os botões
    col1, col2 = st.columns([1, 16])

    with col1:
        # Estilo aplicado apenas ao botão "Entrar"
        if st.button("Entrar", key="login_button"):
            if login(username, password):
                st.session_state.username = username
                go_to_home()
                st.toast("Login bem-sucedido!", icon="✅")
            else:
                st.toast("Usuário ou senha incorretos.", icon="❌")

    with col2:
        if st.button("Cadastrar", key="register_button"):
            go_to_register()

    # Botão extra abaixo das colunas
    if st.button("Esqueci minha senha!", key="forgot_password_button"):
        go_to_new_password()


