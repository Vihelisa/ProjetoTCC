import streamlit as st
from functions.functions import *


def process_register():
    
    topbar('Cadastro de Processos Jurídicos') #função fo estilo do topo do site

    tab1, tab2 = st.tabs(["Cadastro Manual", "Buscar no Jusbrasil"])

    with tab1:
        st.subheader("Cadastro Manual")
        col1, col2, col3 = st.columns(3)
        with col1:
            process_number = st.text_input("Número do Processo", key="process_number")
            lawyer_name = st.text_input("Nome do Advogado", key="lawyer_name")
            proess_path = st.selectbox(
                "Escolha o Caminho Processual:",
                ["Opção 1", "Opção 2", "Opção 3"]
            )
            case_value = st.text_input("Valor da Causa", key="case_value")

        with col2:
            process_class = st.selectbox(
                "Escolha a Classe do Processo:",
                ["Opção 1", "Opção 2", "Opção 3"]
            )
            num_oab = st.text_input("Número da OAB:", key="num_oab")
            judge_name = st.text_input("Nome do Juiz:", key="judge_name")
            def_case_value = st.text_input("Valor Deferido da Causa:", key="def_case_value")

        with col3:
            process_rito = st.selectbox(
                "Escolha o Rito do Processo:",
                ["Ordinário", "Sumário", "Sumaríssimo"]
            )
            customer_name = st.text_input("Nome do(a) Client/Empresa:", key="customer_name")
            state_name = st.selectbox(
                "Escolha o Estado em que corre o processo:",
                ["SP", "RJ", "SC", "MG", "RS", "PR", "BA", "PE", "CE", "DF"]
            )
            payed_value = st.text_input("Valor Pago pela Causa:", key="payed_value")

        obs = st.text_area("Observações sobre o Caso:", key="obs")
        if st.button("Cadastrar Processo"):
                st.success("Processo cadastrado com sucesso!")


    with tab2:
        st.subheader("Buscar no Jusbrasil")
        