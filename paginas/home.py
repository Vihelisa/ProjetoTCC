import streamlit as st

from config.auth import *
from functions.functions import *




def home():

    # Estilo do topo
    topbar("Página Inicial") #função fo estilo do topo do site
    st.title("Bem-vindo ao JurisDash!")
   
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("O que é o JurisDash?")
        st.write("""
            O JurisDash é uma plataforma inovadora de visualização de dados jurídicos, 
            projetada para facilitar o acesso e a análise de informações processuais. 
            Com uma interface intuitiva e recursos avançados, o JurisDash permite que 
            profissionais do direito explorem dados de forma eficiente e eficaz.
        """)
        
        
    with col2:
        st.subheader("Funcionalidades Principais")
        st.write("""
            - **Visualização de Processos**: Acompanhe o histórico e o status dos processos de forma clara e organizada.
            - **Análise de Dados**: Utilize gráficos e tabelas para entender tendências e padrões nos dados jurídicos.
            - **Integração com Sistemas Judiciais**: Conecte-se facilmente a bases de dados judiciais para obter informações atualizadas.
            - **Interface Intuitiva**: Navegação simples e amigável, projetada para usuários de todos os níveis de experiência.
        """)