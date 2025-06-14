import streamlit as st
from PIL import Image
from auth import login, register
from io import BytesIO
import base64

def go_to_login():
    st.session_state.page = "login"

def go_to_register():
    st.session_state.page = "register"

def go_to_home():
    st.session_state.page = "home"
    st.session_state.logged_in = True

def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def password_page():
    image = Image.open("title.png")

    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{image_to_base64(image)}" width="350">
        </div>
        """,unsafe_allow_html=True)

    st.title("Nova Senha")
    new_password = st.text_input("Digite sua nova senha:")
    password = st.text_input("Confirme nova senha:", type="password")
    if st.button("Registrar"):
        if register(new_password, password):
            st.success("Cadastro realizado com sucesso!")
            go_to_login()
        else:
            st.error("Erro ao cadastrar nova senha.")
    if st.button("Voltar"):
        go_to_login()
