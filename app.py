import streamlit as st
from auth import login, register
from paginas.home import home
from paginas.pagina1 import pagina1
from paginas.pagina2 import pagina2
from login import login_page
from register import register_page
from new_password import password_page

st.markdown("""
    <style>
    * {
        color: #0B046E !important;
    }
    </style>
""", unsafe_allow_html=True)



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

def go_to_new_password():
    st.session_state.page = "password"

def go_to_home():
    st.session_state.page = "home"
    st.session_state.logged_in = True


def main_app():
    st.sidebar.title(f"Bem-vindo, {st.session_state.username}")
    page = st.sidebar.radio("Navegar para:", ["Página Inicial", "Página 1", "Página 2"])
    if page == "Página Inicial":
        home()
    elif page == "Página 1":
        pagina1()
    elif page == "Página 2":
        pagina2()

if st.session_state.page == "login":
    login_page()
elif st.session_state.page == "register":
    register_page()
elif st.session_state.page == "password":
    password_page()
elif st.session_state.page == "home" and st.session_state.logged_in:
    main_app()
else:
    go_to_login()
    login_page()
