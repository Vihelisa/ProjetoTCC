import streamlit as st
import requests
from requests.auth import HTTPBasicAuth


from functions.functions import *
from config.auth import *

token_acesso = "cDZHYzlZa0JadVREZDJCendQbXY6SkJlTzNjLV9TRENyQk1RdnFKZGRQdw=="


def process_register():
    conn_user, cursor_user = conect_database_with_user()
    df_estados, df_class_process, df_path_process, df_datajud_endpoints = make_db_register(cursor_user)
    sigla_estados_list = df_estados['SIGLA_ESTADO'].tolist()
    class_process_list = df_class_process['CLASSE_PROCESSO'].tolist()
    path_process_list = df_path_process['CAMINHO_PROCESSUAL'].tolist()
    df_justice = df_datajud_endpoints.groupby("JUSTICA")["TRIBUNAL"].count().reset_index(name="quantidade_tribunais")
    justice_list = df_justice['JUSTICA'].tolist()


    topbar('Cadastro de Processos Jurídicos') #função fo estilo do topo do site

    tab1, tab2 = st.tabs(["Cadastro Manual", "Consultas Externas"])

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
        st.subheader("Consulta de Processo - API Pública do CNJ (Conselho Nacional de Justiça)")

        st.markdown("Digite o número do processo no formato **00000000000000000000** (sem caracteres especiais) para consultar os dados disponíveis na API pública do CNJ (DataJud).")

        numero_processo = st.text_input("Número do Processo (CNJ):")
        justice = st.selectbox("Selecione uma opção de Justiça:", justice_list)
        tribunal_list = df_datajud_endpoints[df_datajud_endpoints['JUSTICA'] == justice]['TRIBUNAL'].unique().tolist() 
        tribunal = st.selectbox("Selecione o Tribunal:", tribunal_list)
        url = df_datajud_endpoints[df_datajud_endpoints['TRIBUNAL'] == tribunal]['ENDPOINT'].reset_index(drop=True).values[0]

        if st.button("Consultar"):
            if numero_processo:
                with st.spinner("Consultando processo..."):
                    headers = {
                        "Authorization": f"APIKey {token_acesso}",
                        "Content-Type": "application/json"
                    }
                    body_json = {
                        "query": {
                            "match": {
                                "numeroProcesso": numero_processo
                            }
                        }
                    }
                    response = requests.post(url, headers=headers, json=body_json)

                    if response.status_code == 200:
                        dados = response.json()
                        if dados:
                            dict_hits = dados.get('hits', {}).get('hits', [])
                            if not dict_hits:
                                st.warning("Não há dados relacionados a esse número de processo.")
                            else:
                                dict_hits = dict_hits[0].get('_source', {})
                                st.json(dict_hits)

                                # Processar os dados para tabela
                                movimentos = dict_hits.get("movimentos", [])
                                linhas = []

                                for mov in movimentos:
                                    base = {
                                        "dataHora": mov.get("dataHora"),
                                        "nome": mov.get("nome"),
                                        "codigo": mov.get("codigo")
                                    }
                                    complementos = mov.get("complementosTabelados", [])
                                    if complementos:
                                        for comp in complementos:
                                            linha = base.copy()
                                            linha.update({
                                                "complemento_nome": comp.get("nome"),
                                                "complemento_descricao": comp.get("descricao"),
                                                "complemento_valor": comp.get("valor")
                                            })
                                            linhas.append(linha)
                                    else:
                                        linhas.append(base)

                                df_movimentos = pd.DataFrame(linhas)

                                # Exibir no Streamlit
                                st.title("📄 Movimentos Processuais")
                                st.dataframe(df_movimentos)

                        else:
                            st.warning("Nenhum dado encontrado para esse número de processo.")
                    else:
                        st.error(f"Erro ao consultar a API: {response.status_code}")
            else:
                st.warning("Por favor, insira um número de processo válido.")

                