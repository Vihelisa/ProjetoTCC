import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

from functions.functions import *
from paginas.home import conn_user, cursor_user
from config.auth import make_db_process

# Simulação de dados do banco
df_process = make_db_process(cursor_user)

def process_history():
    topbar("Histórico de Processos") #função fo estilo do topo do site

    tab1, tab2 = st.tabs(["Todos os Processos", "Atualização de Processo"])

    with tab1:
        st.subheader("Cadastro Manual")
        # Selecionar processo para editar
        opcoes = ["Todos"]
        opcoes_df = df_process["NUMERO_PROCESSO"].tolist()
        opcoes_list = opcoes + opcoes_df
        selecionado = st.selectbox("Selecione um processo para editar:", opcoes_list)

        if selecionado == "Todos":
            # Exibir todos os processos
            # Exibir tabela
            st.dataframe(df_process.drop(columns=["NUMERO_PROCESSO"]), use_container_width=True)
        else:
            # Exibir apenas o processo selecionado
            df_selecionado = df_process[df_process["NUMERO_PROCESSO"] == selecionado]
            if not df_selecionado.empty:
                st.dataframe(df_selecionado.drop(columns=["NUMERO_PROCESSO"]), use_container_width=True)
            else:
                st.warning("Nenhum processo encontrado com o número selecionado.")

        # Dados do processo selecionado
        #processo = df_process[df_process["NUMERO_PROCESSO"] == selecionado].iloc[0]



    with tab2:
        opcoes_df = df_process["NUMERO_PROCESSO"].tolist()
        selecionado = st.selectbox("Selecione um processo para editar:", opcoes_df)
        df_selecionado = df_process[df_process["NUMERO_PROCESSO"] == selecionado].reset_index(drop=True)
        with st.form("editar_processo"):
            st.markdown("### Editar Processo")
            novo_cliente = st.text_input("Cliente", df_selecionado["NOME_CLIENTE_EMPRESA"][0])
            """
            nova_acao = st.text_input("Ação/Fórum", processo["Ação/Fórum"])
            nova_data = st.date_input("Última Atualização")"""

            salvar = st.form_submit_button("Salvar Alterações")

            if salvar:
                # Aqui você atualizaria o banco de dados com os novos valores
                st.success("Processo atualizado com sucesso!")
    
