import streamlit as st
from functions.functions import *
from config.auth import *


def dashboard():
    conn_user, cursor_user = conect_database_with_user()
    df_process = make_db_process(cursor_user)

    topbar("Dashboard") #função fo estilo do topo do site

    st.subheader("Processos relacionados ao usuário:")
    df_process_count = df_process.groupby('CLASSE_PROCESSO').size().reset_index(name='QUANTIDADE_PROCESSOS')
    total_processos = df_process.shape[0]
    st.write(f'Total de processos até o momento são de: {total_processos}')
    st.dataframe(df_process_count, use_container_width=True)