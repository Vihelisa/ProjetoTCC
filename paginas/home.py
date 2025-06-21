import streamlit as st

from config.auth import database_conection, make_db_highq_login
from functions.functions import *

conn, cursor = database_conection()
df_login_user_data, df_user_bd = make_db_highq_login(cursor)
username = st.session_state.username
user_bd_login = df_login_user_data[df_login_user_data['EMAIL'] == username]['USERNAME'].values[0]
print(f"Usuário logado: {username}")
conn_user, cursor_user = database_conection(user_bd_login, user_bd_login)

def home():
    # Estilo do topo
    topbar("Página Inicial") #função fo estilo do topo do site
   
