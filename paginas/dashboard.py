import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from functions.functions import *
from functions.analises import carregar_processos, formatar_brl, meses_do_periodo, taxa_exito_por_area, ENCERRADO, EM_ABERTO


def dashboard():
    conn_user, cursor_user = conect_database_with_user()
    df = carregar_processos(cursor_user)
    _, _, df_path_process, _ = make_db_register(cursor_user)

    topbar("Dashboard") #função fo estilo do topo do site

    if df is None:
        st.error("Não foi possível carregar os dados do dashboard.")
        return
    if df.empty:
        st.info("Nenhum processo cadastrado ainda.")
        return

    total = len(df)
    em_aberto = int((df["STATUS"] == EM_ABERTO).sum())
    deferidos = int((df["VALOR_DEFERIDO_CAUSA"] > 0).sum())
    encerrados = total - em_aberto
    taxa_global = encerrados / total * 100

    st.subheader("Visão Geral dos Processos")
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Total de Processos", total)
    col2.metric("Em Aberto", em_aberto)
    col3.metric("Deferidos", deferidos)
    col4.metric("Encerrados com Recebimento", encerrados)
    col5.metric("Taxa Global de Êxito", f"{taxa_global:.1f}%")

    st.subheader("Distribuição por Área Jurídica")
    col_esq, col_dir = st.columns(2)
    por_area = df["CLASSE_PROCESSO"].value_counts().reset_index()
    por_area.columns = ["Área", "Processos"]
    with col_esq:
        fig = px.pie(por_area, names="Área", values="Processos", hole=0.45,
                     title="% de Processos por Área")
        st.plotly_chart(fig, use_container_width=True)
    with col_dir:
        fig = px.bar(por_area.sort_values("Processos"), x="Processos", y="Área", orientation="h",
                     title="Quantidade de Processos por Área")
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Etapas Processuais e Evolução Temporal")
    col_esq, col_dir = st.columns(2)
    etapas_ordem = df_path_process["CAMINHO_PROCESSUAL"].tolist()
    por_etapa = df["CAMINHO_PROCESSUAL"].value_counts().reindex(etapas_ordem, fill_value=0).reset_index()
    por_etapa.columns = ["Etapa", "Processos"]
    por_etapa = por_etapa[por_etapa["Processos"] > 0]
    with col_esq:
        fig = px.funnel(por_etapa, x="Processos", y="Etapa", title="Processos por Etapa Processual")
        st.plotly_chart(fig, use_container_width=True)

    with col_dir:
        meses = meses_do_periodo(df)
        novos = df.groupby("MES").size().reindex(meses, fill_value=0)
        serie = pd.DataFrame({
            "Mês": novos.index.astype(str),
            "Novos processos": novos.values,
            "Total acumulado": novos.cumsum().values,
        })
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_bar(x=serie["Mês"], y=serie["Novos processos"], name="Novos no mês", secondary_y=False)
        fig.add_scatter(x=serie["Mês"], y=serie["Total acumulado"], name="Acumulado", mode="lines+markers",
                        secondary_y=True)
        fig.update_layout(title="Novos Processos por Mês")
        fig.update_yaxes(title_text="Novos processos", secondary_y=False)
        fig.update_yaxes(title_text="Total acumulado", secondary_y=True)
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Magistrados e Tribunais")
    col_esq, col_dir = st.columns(2)
    with col_esq:
        juizes = df["NOME_JUIZ"].value_counts().head(10).reset_index()
        juizes.columns = ["Juiz", "Processos"]
        fig = px.bar(juizes.sort_values("Processos"), x="Processos", y="Juiz", orientation="h",
                     title="Top 10 Processos por Juiz")
        st.plotly_chart(fig, use_container_width=True)
    with col_dir:
        tribunais = df.groupby("TRIBUNAL", as_index=False).size().rename(columns={"size": "Processos"})
        fig = px.treemap(tribunais, path=["TRIBUNAL"], values="Processos",
                         title="Processos por Tribunal")
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Probabilidade e Taxa de Êxito")
    tabela = taxa_exito_por_area(df)
    col_esq, col_dir = st.columns(2)
    with col_esq:
        fig = px.bar(tabela.sort_values("PROB_EXITO"), x="PROB_EXITO", y="CLASSE_PROCESSO", orientation="h",
                     title="Taxa de Êxito por Área (%)", labels={"PROB_EXITO": "% com recebimento", "CLASSE_PROCESSO": "Área"})
        st.plotly_chart(fig, use_container_width=True)
    with col_dir:
        rito = df.groupby("RITO_PROCESSO").agg(
            Total=("NUMERO_PROCESSO", "count"),
            **{"Com recebimento": ("STATUS", lambda s: (s == ENCERRADO).sum())},
        ).reset_index()
        fig = go.Figure()
        fig.add_bar(x=rito["RITO_PROCESSO"], y=rito["Total"], name="Total", marker_color="#B8B3E9")
        fig.add_bar(x=rito["RITO_PROCESSO"], y=rito["Com recebimento"], name="Com recebimento",
                    marker_color="#0B046E")
        fig.update_layout(barmode="overlay", title="Probabilidade de Êxito por Rito Processual",
                          xaxis_title="Rito", yaxis_title="Processos")
        st.plotly_chart(fig, use_container_width=True)

    col_esq, col_dir = st.columns(2)
    with col_esq:
        cruzada = pd.crosstab(df["CLASSE_PROCESSO"], df["CAMINHO_PROCESSUAL"]).reindex(columns=etapas_ordem, fill_value=0)
        fig = px.imshow(cruzada, text_auto=True, aspect="auto", color_continuous_scale="Blues",
                        title="Mapa de Calor: Área × Etapa Processual",
                        labels={"x": "Etapa", "y": "Área", "color": "Processos"})
        st.plotly_chart(fig, use_container_width=True)
    with col_dir:
        por_uf = df["ESTADO_PROCESSO"].value_counts().reset_index()
        por_uf.columns = ["UF", "Processos"]
        fig = px.bar(por_uf, x="UF", y="Processos", title="Processos por Estado (UF)")
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Estimativa de Probabilidade de Êxito")
    st.caption("Estimativa baseada no histórico de processos encerrados com recebimento.")
    tabela_exibicao = tabela.rename(columns={
        "CLASSE_PROCESSO": "Área Jurídica",
        "PROCESSOS": "Processos",
        "ENCERRADOS": "Encerrados c/ ganho",
        "DEFERIDOS": "Deferidos",
        "EM_ABERTO": "Em aberto",
        "VALOR_MEDIO_CAUSA": "Valor médio em causa (R$)",
        "VALOR_MEDIO_RECEBIDO": "Valor médio recebido (R$)",
        "PROB_EXITO": "Prob. êxito (%)",
    })
    st.dataframe(tabela_exibicao, use_container_width=True, hide_index=True, column_config={
        "Prob. êxito (%)": st.column_config.NumberColumn(format="%.1f"),
        "Valor médio em causa (R$)": st.column_config.NumberColumn(format="R$ %.2f"),
        "Valor médio recebido (R$)": st.column_config.NumberColumn(format="R$ %.2f"),
    })

    area_selecionada = st.selectbox("Selecione a área:", tabela["CLASSE_PROCESSO"].tolist())
    prob = float(tabela.loc[tabela["CLASSE_PROCESSO"] == area_selecionada, "PROB_EXITO"].iloc[0])
    media_geral = encerrados / total * 100
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=prob,
        number={"suffix": "%"},
        delta={"reference": media_geral, "suffix": "% vs. média geral"},
        title={"text": f"Probabilidade estimada: {area_selecionada}"},
        gauge={"axis": {"range": [0, 100]}, "bar": {"color": "#0B046E"}},
    ))
    st.plotly_chart(fig, use_container_width=True)
