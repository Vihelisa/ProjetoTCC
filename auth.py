# auth.py
import streamlit as st
import json
import os

USERS_FILE = "data/users.json"

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
