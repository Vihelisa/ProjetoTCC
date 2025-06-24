import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

from functions.functions import *
from config.auth import make_db_process

# Simulação de dados do banco

def process_history():
    conn_user, cursor_user = conect_database_with_user()
    df_process = make_db_process(cursor_user)
    df_estados, df_class_process, df_path_process = make_db_register(cursor_user)

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
        path_process_list = df_path_process['CAMINHO_PROCESSUAL'].tolist()
        selecionado = st.selectbox("Selecione um processo para editar:", opcoes_df)
        df_selecionado = df_process[df_process["NUMERO_PROCESSO"] == selecionado].reset_index(drop=True)
        with st.form("editar_processo"):
            st.markdown("### Editar Processo")
            process_path = st.selectbox("Escolha o Caminho Processual:", path_process_list)
            case_value = st.text_input("Valor da Causa", df_selecionado["VALOR_CAUSA"][0])
            def_case_value = st.text_input("Valor Deferido da Causa:", df_selecionado["VALOR_DEFERIDO_CAUSA"][0])
            payed_value = st.text_input("Valor Pago pela Causa:", df_selecionado["VALOR_PAGO_CAUSA"][0])
            judge_name = st.text_input("Nome do Juiz:", df_selecionado["NOME_JUIZ"][0])
            obs = st.text_area("Observações sobre o Caso:", df_selecionado["OBSERVACOES_CLOB"][0])

            
            salvar = st.form_submit_button("Salvar Alterações")

            if salvar:
                # Aqui você atualizaria o banco de dados com os novos valores
                st.success("Processo atualizado com sucesso!")
    
