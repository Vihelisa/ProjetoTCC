import streamlit as st
from functions.functions import *
from config.auth import *



def process_register():
    conn_user, cursor_user = conect_database_with_user()
    df_estados, df_class_process, df_path_process = make_db_register(cursor_user)
    sigla_estados_list = df_estados['SIGLA_ESTADO'].tolist()
    class_process_list = df_class_process['CLASSE_PROCESSO'].tolist()
    path_process_list = df_path_process['CAMINHO_PROCESSUAL'].tolist()

    topbar('Cadastro de Processos Jurídicos') #função fo estilo do topo do site

    tab1, tab2 = st.tabs(["Cadastro Manual", "Buscar no Jusbrasil"])

    with tab1:
        st.subheader("Cadastro Manual")
        col1, col2, col3 = st.columns(3)
        with col1:
            process_number = st.text_input("Número do Processo", key="process_number")
            lawyer_name = st.text_input("Nome do Advogado", key="lawyer_name")
            process_path = st.selectbox("Escolha o Caminho Processual:", path_process_list)
            case_value = st.text_input("Valor da Causa", key="case_value")

        with col2:
            process_class = st.selectbox("Escolha a Classe do Processo:", class_process_list)
            num_oab = st.text_input("Número da OAB:", key="num_oab")
            judge_name = st.text_input("Nome do Juiz:", key="judge_name")
            def_case_value = st.text_input("Valor Deferido da Causa:", key="def_case_value")

        with col3:
            process_rito = st.selectbox(
                "Escolha o Rito do Processo:",
                ["Ordinário", "Sumário", "Sumaríssimo"]
            )
            customer_name = st.text_input("Nome do(a) Cliente/Empresa:", key="customer_name")
            state_name = st.selectbox("Escolha o Estado em que corre o processo:", sigla_estados_list)
            payed_value = st.text_input("Valor Pago pela Causa:", key="payed_value")

        obs = st.text_area("Observações sobre o Caso:", key="obs")
        
        uploaded_file = st.file_uploader("Faça upload do PDF do processo", type=["pdf"])
        
        if uploaded_file is not None:
            st.success(f"Arquivo '{uploaded_file.name}' carregado com sucesso!")
            pdf_bytes = uploaded_file.read()
            nome_arquivo = uploaded_file.name

        if st.button("Cadastrar Processo"):
            try:
                dict_prc_register_process(conn_user, cursor_user, process_number, lawyer_name, process_path, case_value,
                              process_class, num_oab, judge_name, def_case_value,
                              process_rito, customer_name, state_name, payed_value,
                              obs, pdf_bytes, nome_arquivo)
                st.success("Processo cadastrado com sucesso!")
            except Exception as e:
                st.error(f"Erro ao cadastrar o processo: {e}")
                print(f"Erro ao cadastrar o processo: {e}")

            



    with tab2:
        st.subheader("Buscar no Jusbrasil")
        