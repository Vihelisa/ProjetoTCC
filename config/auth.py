# auth.py
import streamlit as st
import json
import os
import cx_Oracle
import pandas as pd

USERS_FILE = "data/users.json"

def database_conection(user_bd='admin', password_bd='admin', tns_bd='DKR_NAC_213'):
    try:
        conn = cx_Oracle.connect(user=str(user_bd), password=str(password_bd), dsn=str(tns_bd))
        cursor = conn.cursor()
        return conn, cursor
    except cx_Oracle.DatabaseError as e:
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

    except cx_Oracle.DatabaseError as e:
        return None
    

def make_db_highq_login(cursor):

    #script_dir = os.path.dirname(__file__)
    file_path = os.path.join('config/query.json')

    with open(file_path) as file:
        querys = json.load(file)

    
    df_login_user_data = get_data(querys['loginUserData'], cursor)
    df_user_bd = get_data(querys['userBD'], cursor)
    return df_login_user_data, df_user_bd


def make_db_register(cursor):

    #script_dir = os.path.dirname(__file__)
    file_path = os.path.join('config/query.json')

    with open(file_path) as file:
        querys = json.load(file)
    
    df_estados = get_data(querys['estadosBR'], cursor)
    df_class_process = get_data(querys['classProcess'], cursor)
    df_path_process = get_data(querys['pathProcess'], cursor)
    return df_estados, df_class_process, df_path_process


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
    if username in df_login_user_data['EMAIL'].to_list() and password in df_login_user_data['LOGIN_PASSWORD'].to_list():
        print("Usuário encontrado no banco de dados.")
        return True
    else: 
        print("Usuário ou senha inválidos.") 
        return False


def insert_user_data(conn, cursor, register_dict):
    sql = f"""
        INSERT INTO login_user_data(NAME, EMAIL, LOGIN_PASSWORD, NUM_OAB, USERNAME)
        VALUES (:1, :2, :3, :4, :5)
    """
    try:
        cursor.execute(sql, (register_dict['nome'], register_dict['email'], register_dict['senha'], register_dict['num_oab'], register_dict['username']))
        conn.commit()
    except cx_Oracle.IntegrityError:
        st.toast("Erro ao tentar fazer cadastro de novo usuário!", icon="❌")
        return False
    return True


def insert_db_user(conn, cursor, register_bd_dict):
    sql = f"""
        INSERT INTO users(USERNAME, PASSWORD)
        VALUES (:1, :2)
    """
    try:
        cursor.execute(sql, (register_bd_dict['username'], register_bd_dict['password']))
        conn.commit()
    except cx_Oracle.IntegrityError:
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
