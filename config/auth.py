# auth.py
import streamlit as st
import json
import os
import cx_Oracle

USERS_FILE = "data/users.json"

def database_conection(user_bd, password_bd, tns_bd):
    try:
        conn = cx_Oracle.connect(user=str(user_bd), password=str(password_bd), dsn=str(tns_bd))
        cursor = conn.cursor()
        return conn, cursor
    except cx_Oracle.DatabaseError as e:
        return None, None

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

def login(username, password):
    users = load_users()
    return users.get(username) == password

def register(username, password):
    users = load_users()
    if username in users:
        return False
    users[username] = password
    save_users(users)
    return True
