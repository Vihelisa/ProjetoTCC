import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

from auth import login, register
from login import login_page
from register import register_page
from new_password import password_page
from paginas.home import home
from paginas.process_register import process_register
from paginas.process_history import process_history
from paginas.dashboard import dashboard
from paginas.user_profile import user_profile



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
    with st.sidebar:
        st.markdown(f"### 👋 Bem-vindo, {st.session_state.username}")
        page = option_menu(
            menu_title=None,
            options=["Área de Trabalho", "Cadastro de Processos", "Histórico de Processos", "Dashboard", "Perfil do Usuário"],
            styles={
            "container": {"background-color": "#f0f2f6", 'width':"100%"},
            "nav-link": {"font-size": "15px", "text-align": "center", 'width':"100%"},
            "nav-link-selected": {"background-color": "#0B046E", "color": "white", 'width':"100%"},
            }
        )
    if page == "Área de Trabalho":
        home()
    elif page == "Cadastro de Processos":
        process_register()
    elif page == "Histórico de Processos":
        process_history()
    elif page == "Dashboard":
        dashboard()
    elif page == "Perfil do Usuário":
        user_profile()

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
