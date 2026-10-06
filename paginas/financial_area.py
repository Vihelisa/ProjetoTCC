import streamlit as st
import pandas as pd
import plotly.express as px

from functions.functions import *
from functions.analises import carregar_processos, formatar_brl, meses_do_periodo, ENCERRADO, EM_ABERTO


def financial_area():
    conn_user, cursor_user = conect_database_with_user()
    df = carregar_processos(cursor_user)

    topbar("Área Financeira") #função fo estilo do topo do site

    if df is None:
        st.error("Não foi possível carregar os dados financeiros.")
        return
    if df.empty:
        st.info("Nenhum processo cadastrado ainda.")
        return

    st.subheader("Resumo Geral")
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Total de Processos", len(df))
    col2.metric("Valor Total em Causa", formatar_brl(df["VALOR_CAUSA"].sum()))
    col3.metric("Total Deferido", formatar_brl(df["VALOR_DEFERIDO_CAUSA"].sum()))
    col4.metric("Total Recebido", formatar_brl(df["VALOR_PAGO_CAUSA"].sum()))
    col5.metric("Em Aberto (causa)", formatar_brl(df.loc[df["STATUS"] == EM_ABERTO, "VALOR_CAUSA"].sum()))

    col_esq, col_dir = st.columns(2)
    with col_esq:
        participacao = df.groupby("CLASSE_PROCESSO", as_index=False)["VALOR_CAUSA"].sum()
        fig = px.pie(participacao, names="CLASSE_PROCESSO", values="VALOR_CAUSA", hole=0.45,
                     title="Participação por Área Jurídica (% do valor em causa)")
        st.plotly_chart(fig, use_container_width=True)

    with col_dir:
        por_area = df.groupby("CLASSE_PROCESSO", as_index=False)[
            ["VALOR_CAUSA", "VALOR_DEFERIDO_CAUSA", "VALOR_PAGO_CAUSA"]].sum()
        por_area = por_area.melt(id_vars="CLASSE_PROCESSO", var_name="Tipo", value_name="Valor")
        por_area["Tipo"] = por_area["Tipo"].map({
            "VALOR_CAUSA": "Valor em causa",
            "VALOR_DEFERIDO_CAUSA": "Valor deferido",
            "VALOR_PAGO_CAUSA": "Valor recebido",
        })
        fig = px.bar(por_area, x="CLASSE_PROCESSO", y="Valor", color="Tipo", barmode="group",
                     title="Valores por Área Jurídica", labels={"CLASSE_PROCESSO": "Área", "Valor": "R$"})
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Indicadores Financeiros")
    col_esq, col_dir = st.columns(2)

    with col_esq:
        meses = meses_do_periodo(df)
        mensal = df.groupby("MES")[["VALOR_CAUSA", "VALOR_DEFERIDO_CAUSA", "VALOR_PAGO_CAUSA"]].sum()
        mensal = mensal.reindex(meses, fill_value=0).cumsum()
        mensal.index = mensal.index.astype(str)
        mensal.index.name = "Mês"
        mensal = mensal.reset_index().melt(id_vars="Mês", var_name="Tipo", value_name="Valor")
        mensal["Tipo"] = mensal["Tipo"].map({
            "VALOR_CAUSA": "Causa acumulada",
            "VALOR_DEFERIDO_CAUSA": "Deferido acumulado",
            "VALOR_PAGO_CAUSA": "Recebido acumulado",
        })
        fig = px.line(mensal, x="Mês", y="Valor", color="Tipo", markers=True,
                      title="Evolução Mensal de Valores (acumulado)", labels={"Valor": "R$"})
        st.plotly_chart(fig, use_container_width=True)

    with col_dir:
        status = df["STATUS"].value_counts().reset_index()
        status.columns = ["Status", "Processos"]
        fig = px.bar(status, x="Processos", y="Status", orientation="h", color="Status",
                     title="Processos por Status Financeiro")
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    col_esq, col_dir = st.columns(2)
    with col_esq:
        taxa = df.groupby("CLASSE_PROCESSO").agg(
            processos=("NUMERO_PROCESSO", "count"),
            encerrados=("STATUS", lambda s: (s == ENCERRADO).sum()),
        ).reset_index()
        taxa["Taxa de êxito (%)"] = taxa["encerrados"] / taxa["processos"] * 100
        taxa = taxa.sort_values("Taxa de êxito (%)")
        fig = px.bar(taxa, x="Taxa de êxito (%)", y="CLASSE_PROCESSO", orientation="h",
                     title="Taxa de Êxito por Área", text=taxa["Taxa de êxito (%)"].round(1).astype(str) + "%",
                     labels={"CLASSE_PROCESSO": "Área"})
        st.plotly_chart(fig, use_container_width=True)

    with col_dir:
        ramo = df.groupby("JUSTICA", as_index=False)["VALOR_CAUSA"].sum()
        fig = px.treemap(ramo, path=["JUSTICA"], values="VALOR_CAUSA",
                         title="Distribuição dos Valores por Ramo da Justiça")
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Detalhamento Financeiro por Processo")
    detalhe = df[["NUMERO_PROCESSO", "CLASSE_PROCESSO", "NOME_CLIENTE_EMPRESA", "CAMINHO_PROCESSUAL",
                  "VALOR_CAUSA", "VALOR_DEFERIDO_CAUSA", "VALOR_PAGO_CAUSA", "STATUS"]].rename(columns={
        "NUMERO_PROCESSO": "Nº Processo",
        "CLASSE_PROCESSO": "Classe",
        "NOME_CLIENTE_EMPRESA": "Cliente/Empresa",
        "CAMINHO_PROCESSUAL": "Etapa",
        "VALOR_CAUSA": "Valor da Causa (R$)",
        "VALOR_DEFERIDO_CAUSA": "Valor Deferido (R$)",
        "VALOR_PAGO_CAUSA": "Valor Recebido (R$)",
        "STATUS": "Situação",
    })
    st.dataframe(detalhe, use_container_width=True, hide_index=True)
    st.markdown(
        f"**Totais:** Causa {formatar_brl(df['VALOR_CAUSA'].sum())} · "
        f"Deferido {formatar_brl(df['VALOR_DEFERIDO_CAUSA'].sum())} · "
        f"Recebido {formatar_brl(df['VALOR_PAGO_CAUSA'].sum())}"
    )
