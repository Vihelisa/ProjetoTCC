import pandas as pd

from config.auth import make_db_process

ENCERRADO = "Encerrado com recebimento"
EM_ABERTO = "Em aberto"


def formatar_brl(valor):
    texto = f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


def carregar_processos(cursor):
    df = make_db_process(cursor)
    if df is None or df.empty:
        return None

    df = df.copy()
    for coluna in ["VALOR_CAUSA", "VALOR_DEFERIDO_CAUSA", "VALOR_PAGO_CAUSA"]:
        df[coluna] = pd.to_numeric(df[coluna], errors="coerce").fillna(0.0)

    df["DATA_CADASTRO"] = pd.to_datetime(df["DATA_CADASTRO"])
    df["MES"] = df["DATA_CADASTRO"].dt.to_period("M")
    df["STATUS"] = (df["VALOR_PAGO_CAUSA"] > 0).map({True: ENCERRADO, False: EM_ABERTO})
    return df


def meses_do_periodo(df):
    return pd.period_range(df["MES"].min(), df["MES"].max(), freq="M")


def taxa_exito_por_area(df):
    agrupado = df.groupby("CLASSE_PROCESSO").agg(
        PROCESSOS=("NUMERO_PROCESSO", "count"),
        ENCERRADOS=("STATUS", lambda s: (s == ENCERRADO).sum()),
        DEFERIDOS=("VALOR_DEFERIDO_CAUSA", lambda s: (s > 0).sum()),
        EM_ABERTO=("STATUS", lambda s: (s == EM_ABERTO).sum()),
        VALOR_MEDIO_CAUSA=("VALOR_CAUSA", "mean"),
        VALOR_MEDIO_RECEBIDO=("VALOR_PAGO_CAUSA", "mean"),
    ).reset_index()
    agrupado["PROB_EXITO"] = agrupado["ENCERRADOS"] / agrupado["PROCESSOS"] * 100
    return agrupado.sort_values("PROB_EXITO", ascending=False).reset_index(drop=True)
