import streamlit as st
from PIL import Image
from auth import login, register
from io import BytesIO
import base64


def go_to_home():
    st.session_state.page = "home"
    st.session_state.logged_in = True

def go_to_register():
    st.session_state.page = "register"


def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()


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
    if st.button("Entrar"):
        if login(username, password):
            st.session_state.username = username
            go_to_home()
            st.success("Login bem-sucedido!")
        else:
            st.error("Usuário ou senha incorretos.")
    if st.button("Cadastrar"):
        go_to_register()
