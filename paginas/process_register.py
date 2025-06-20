import streamlit as st
from functions.functions import *


def process_register():
    
    topbar('Cadastro de Processos Jurídicos') #função fo estilo do topo do site

    tab1, tab2 = st.tabs(["Cadastro Manual", "Buscar no Jusbrasil"])

    with tab1:
        st.subheader("Cadastro Manual")
        

    with tab2:
        st.subheader("Buscar no Jusbrasil")
        