# auth.py
import streamlit as st
import json
import os
import sqlite3
import pandas as pd

from config import seed_data

USERS_FILE = "data/users.json"
DB_FILE = os.path.join("data", "app.db")

_db_initialized = False


def _create_schema(conn):
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS login_user_data (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT NOT NULL,
            EMAIL TEXT NOT NULL UNIQUE,
            LOGIN_PASSWORD TEXT NOT NULL,
            NUM_OAB TEXT,
            USERNAME TEXT NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS users (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            USERNAME TEXT UNIQUE,
            PASSWORD TEXT
        );

        CREATE TABLE IF NOT EXISTS estados_brasil (
            NOME_ESTADO TEXT NOT NULL,
            SIGLA_ESTADO TEXT PRIMARY KEY
        );

        CREATE TABLE IF NOT EXISTS classes_processo (
            CLASSE_PROCESSO TEXT PRIMARY KEY
        );

        CREATE TABLE IF NOT EXISTS caminho_processo (
            CAMINHO_PROCESSUAL TEXT PRIMARY KEY
        );

        CREATE TABLE IF NOT EXISTS processos_juridicos (
            NUMERO_PROCESSO TEXT PRIMARY KEY,
            CLASSE_PROCESSO TEXT,
            RITO_PROCESSO TEXT,
            NOME_ADVOGADO TEXT,
            NUMERO_OAB TEXT,
            NOME_CLIENTE_EMPRESA TEXT,
            CAMINHO_PROCESSUAL TEXT,
            NOME_JUIZ TEXT,
            ESTADO_PROCESSO TEXT,
            VALOR_CAUSA REAL,
            VALOR_DEFERIDO_CAUSA REAL,
            VALOR_PAGO_CAUSA REAL,
            OBSERVACOES_CLOB TEXT,
            JUSTICA TEXT,
            TRIBUNAL TEXT,
            DATA_CADASTRO TEXT
        );

        CREATE TABLE IF NOT EXISTS arquivos_processos (
            ID_ARQUIVO INTEGER PRIMARY KEY AUTOINCREMENT,
            NUMERO_PROCESSO TEXT,
            NOME_ARQUIVO TEXT,
            ARQUIVO_PDF BLOB,
            FOREIGN KEY (NUMERO_PROCESSO) REFERENCES processos_juridicos (NUMERO_PROCESSO) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS datajud_endpoints (
            JUSTICA TEXT NOT NULL,
            TRIBUNAL TEXT NOT NULL,
            ENDPOINT TEXT NOT NULL
        );
    """)
    colunas = [linha[1] for linha in conn.execute("PRAGMA table_info(processos_juridicos)")]
    if "DATA_CADASTRO" not in colunas:
        conn.execute("ALTER TABLE processos_juridicos ADD COLUMN DATA_CADASTRO TEXT")
    conn.commit()


def _table_is_empty(conn, table):
    return conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0] == 0


def _seed_if_empty(conn):
    if _table_is_empty(conn, "login_user_data"):
        conn.execute(
            "INSERT INTO login_user_data (NAME, EMAIL, LOGIN_PASSWORD, NUM_OAB, USERNAME) VALUES (?, ?, ?, ?, ?)",
            ("admin", "admin@gmail.com", "1234", "0099887766", "admin"),
        )

    if _table_is_empty(conn, "users"):
        conn.execute("INSERT INTO users (USERNAME, PASSWORD) VALUES (?, ?)", ("admin", "admin"))

    if _table_is_empty(conn, "estados_brasil"):
        conn.executemany(
            "INSERT INTO estados_brasil (NOME_ESTADO, SIGLA_ESTADO) VALUES (?, ?)", seed_data.ESTADOS
        )

    if _table_is_empty(conn, "classes_processo"):
        conn.executemany(
            "INSERT INTO classes_processo (CLASSE_PROCESSO) VALUES (?)", seed_data.CLASSES_PROCESSO
        )

    if _table_is_empty(conn, "caminho_processo"):
        conn.executemany(
            "INSERT INTO caminho_processo (CAMINHO_PROCESSUAL) VALUES (?)", seed_data.CAMINHO_PROCESSO
        )

    if _table_is_empty(conn, "datajud_endpoints"):
        conn.executemany(
            "INSERT INTO datajud_endpoints (JUSTICA, TRIBUNAL, ENDPOINT) VALUES (?, ?, ?)",
            seed_data.DATAJUD_ENDPOINTS,
        )

    if _table_is_empty(conn, "processos_juridicos"):
        conn.executemany(
            """
            INSERT INTO processos_juridicos (
                NUMERO_PROCESSO, CLASSE_PROCESSO, RITO_PROCESSO, NOME_ADVOGADO, NUMERO_OAB,
                NOME_CLIENTE_EMPRESA, CAMINHO_PROCESSUAL, NOME_JUIZ, ESTADO_PROCESSO,
                VALOR_CAUSA, VALOR_DEFERIDO_CAUSA, VALOR_PAGO_CAUSA, OBSERVACOES_CLOB,
                JUSTICA, TRIBUNAL, DATA_CADASTRO
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            seed_data.PROCESSOS_TESTE,
        )

    conn.commit()


def _ensure_db():
    global _db_initialized
    if _db_initialized:
        return
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
    conn = sqlite3.connect(DB_FILE)
    _create_schema(conn)
    _seed_if_empty(conn)
    conn.close()
    _db_initialized = True


def database_conection(user_bd=None, password_bd=None, tns_bd=None):
    '''
        Banco de teste local (SQLite) usado para hospedar o projeto no Streamlit
        Community Cloud. Os parâmetros de usuário/senha/TNS do Oracle original
        são aceitos por compatibilidade com o restante do código, mas ignorados:
        aqui existe um único schema compartilhado por todos os usuários.
    '''
    try:
        _ensure_db()
        conn = sqlite3.connect(DB_FILE, check_same_thread=False)
        conn.execute("PRAGMA foreign_keys = ON")
        cursor = conn.cursor()
        return conn, cursor
    except sqlite3.Error:
        return None, None


def get_data(query, cursor):
    '''
        Esta função faz requisições no bano de dados, criando dataframe com as informações obtidas
    '''
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

        df = pd.DataFrame(results, columns=columns)
        return df

    except sqlite3.Error as e:
        return None


def make_db_highq_login(cursor):

    file_path = os.path.join('config/query.json')

    with open(file_path) as file:
        querys = json.load(file)

    df_login_user_data = get_data(querys['loginUserData'], cursor)
    df_user_bd = get_data(querys['userBD'], cursor)
    return df_login_user_data, df_user_bd


def make_db_register(cursor):

    file_path = os.path.join('config/query.json')

    with open(file_path) as file:
        querys = json.load(file)

    df_estados = get_data(querys['estadosBR'], cursor)
    df_class_process = get_data(querys['classProcess'], cursor)
    df_path_process = get_data(querys['pathProcess'], cursor)
    df_datajud_endpoints = get_data(querys['datajudEndpoints'], cursor)
    return df_estados, df_class_process, df_path_process, df_datajud_endpoints


def make_db_process(cursor):

    file_path = os.path.join('config/query.json')

    with open(file_path) as file:
        querys = json.load(file)

    df_process = get_data(querys['processJurid'], cursor)
    return df_process


def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}


def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)


def login(username, password):
    conn, cursor = database_conection()
    df_login_user_data, df_user_bd = make_db_highq_login(cursor)
    password_bd = df_login_user_data[df_login_user_data['EMAIL'] == username]['LOGIN_PASSWORD'].reset_index(drop=True)[0]
    if username in df_login_user_data['EMAIL'].to_list() and password == password_bd:
        print("Usuário encontrado no banco de dados.")
        return True
    else:
        print("Usuário ou senha inválidos.")
        return False


def insert_user_data(conn, cursor, register_dict):
    sql = """
        INSERT INTO login_user_data (NAME, EMAIL, LOGIN_PASSWORD, NUM_OAB, USERNAME)
        VALUES (?, ?, ?, ?, ?)
    """
    try:
        cursor.execute(sql, (register_dict['nome'], register_dict['email'], register_dict['senha'], register_dict['num_oab'], register_dict['username']))
        conn.commit()
    except sqlite3.IntegrityError:
        st.toast("Erro ao tentar fazer cadastro de novo usuário!", icon="❌")
        return False
    return True


def insert_db_user(conn, cursor, register_bd_dict):
    sql = """
        INSERT INTO users (USERNAME, PASSWORD)
        VALUES (?, ?)
    """
    try:
        cursor.execute(sql, (register_bd_dict['username'], register_bd_dict['password']))
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Erro ao tentar inserir usuário no banco de dados: {e}")
        st.toast("Erro ao tentar fazer cadastro de novo usuário!", icon="❌")
        return False
    return True


def register(register_dict, register_bd_dict):
    conn, cursor = database_conection()
    status_insert_user_data = insert_user_data(conn, cursor, register_dict)
    status_db_user = insert_db_user(conn, cursor, register_bd_dict)
    if status_insert_user_data and status_db_user:
        return True
    else:
        st.toast("Erro ao tentar fazer cadastro de novo usuário!", icon="❌")
        return False


def register_new_password(email, new_password):
    conn, cursor = database_conection()
    status_new_password = update_new_password(conn, cursor, email, new_password)
    if status_new_password:
        return True
    else:
        return False


def update_new_password(conn, cursor, email, new_password):
    sql = """
        UPDATE login_user_data
        SET LOGIN_PASSWORD = ?
        WHERE EMAIL = ?
    """
    try:
        cursor.execute(sql, (new_password, email))
        conn.commit()
        return True
    except sqlite3.IntegrityError as e:
        print(f"Erro ao tentar atualizar senha: {e}")
        return False


def update_user_data(conn, cursor, register_dict):
    sql = """
        UPDATE login_user_data
        SET NAME = ?, LOGIN_PASSWORD = ?, NUM_OAB = ?
        WHERE EMAIL = ?
    """
    try:
        cursor.execute(sql, (register_dict['nome'], register_dict['senha'], register_dict['oab'], register_dict['email']))
        conn.commit()
        return True
    except sqlite3.IntegrityError as e:
        print(f"Erro ao tentar atualizar usuário: {e}")
        st.toast("Erro ao tentar fazer cadastro de novo usuário!", icon="❌")
        return False
