import streamlit as st
from auth import login, register
import pages.home as home
import pages.pagina1 as pagina1
import pages.pagina2 as pagina2

if "page" not in st.session_state:
    st.session_state.page = "login"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

def go_to_login():
    st.session_state.page = "login"

def go_to_register():
    st.session_state.page = "register"

def go_to_home():
    st.session_state.page = "home"
    st.session_state.logged_in = True

def login_page():
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

def register_page():
    st.title("Cadastro")
    username = st.text_input("Novo usuário")
    password = st.text_input("Nova senha", type="password")
    if st.button("Registrar"):
        if register(username, password):
            st.success("Cadastro realizado com sucesso!")
            go_to_login()
        else:
            st.error("Usuário já existe.")
    if st.button("Voltar"):
        go_to_login()

def main_app():
    st.sidebar.title(f"Bem-vindo, {st.session_state.username}")
    page = st.sidebar.radio("Navegar para:", ["Página Inicial", "Página 1", "Página 2"])
    if page == "Página Inicial":
        home.show()
    elif page == "Página 1":
        pagina1.show()
    elif page == "Página 2":
        pagina2.show()

if st.session_state.page == "login":
    login_page()
elif st.session_state.page == "register":
    register_page()
elif st.session_state.page == "home" and st.session_state.logged_in:
    main_app()
else:
    go_to_login()
    login_page()
