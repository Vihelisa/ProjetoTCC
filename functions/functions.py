from PIL import Image
from io import BytesIO
import base64
import streamlit as st
import cx_Oracle
from config.auth import *

def conect_database_with_user():
    username = st.session_state.username

    conn, cursor = database_conection()
    df_login_user_data, df_user_bd = make_db_highq_login(cursor)
    user_bd_login = df_login_user_data[df_login_user_data['EMAIL'] == username]['USERNAME'].values[0]
    print(f"Usuário logado: {username}")
    conn_user, cursor_user = database_conection(user_bd_login, user_bd_login)

    return conn_user, cursor_user

def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()


def topbar(titulo):
    image = Image.open("title.png")

    # HTML e CSS para o topo
    st.markdown(f"""
        <style>
            .header {{
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 0px 20px;
                width: 100%;
            }}
            .divider {{
                border-bottom: 1px solid #ccc;
                margin-bottom: 20px;
            }}
            .logo {{
                height: 45px;
            }}
            .titulo-direita{{
                font-size: 35px;
                font-weight: bold;
                color: #0B046E;
            }}
        </style>

        <div class="header">
            <img src="data:image/png;base64,{image_to_base64(image)}" class="logo">
            <div class="titulo-direita">{titulo}</div>
        </div>
        
        <div class="divider"></div>
    """, unsafe_allow_html=True)


def dict_prc_register_process(conn, cursor, process_number, lawyer_name, process_path, case_value,
                              process_class, num_oab, judge_name, def_case_value,
                              process_rito, customer_name, state_name, payed_value,
                              obs, pdf_bytes=None, nome_arquivo=None):
    register_process_dict = {
        'p_numero_processo': process_number,
        'p_nome_advogado': lawyer_name,
        'p_caminho_processual': process_path,
        'p_valor_causa': case_value,
        'p_classe_processo': process_class,
        'p_numero_oab': num_oab,
        'p_nome_juiz': judge_name,
        'p_valor_definido_causa': def_case_value,
        'p_rito_processo': process_rito,
        'p_nome_cliente_empresa': customer_name,
        'p_estado_processo': state_name,
        'p_valor_pago_causa': payed_value,
        'p_observacoes_clob': obs,
        'p_arquivo_pdf': pdf_bytes,
        'p_nome_arquivo': nome_arquivo
    }
    send_values_prc(register_process_dict, conn, cursor)


def send_values_prc(register_process_dict, conn, cursor):
    sql = f"""
        begin
            inserir_processo_com_arquivo(
                p_numero_processo => :p_numero_processo,
                p_classe_processo => :p_classe_processo,
                p_rito_processo  => :p_rito_processo,
                p_nome_advogado  => :p_nome_advogado,
                p_numero_oab => :p_numero_oab,
                p_nome_cliente_empresa => :p_nome_cliente_empresa,
                p_caminho_processual => :p_caminho_processual,
                p_nome_juiz => :p_nome_juiz,
                p_estado_processo => :p_estado_processo,
                p_valor_causa => :p_valor_causa,
                p_valor_definido_causa => :p_valor_definido_causa,
                p_valor_pago_causa=> :p_valor_pago_causa,
                p_observacoes_clob=> :p_observacoes_clob,
                p_nome_arquivo => :p_nome_arquivo,
                p_arquivo_pdf => :p_arquivo_pdf
            );
        end;
    """
    try:
        cursor.execute(sql, register_process_dict)
        conn.commit()
    except cx_Oracle.IntegrityError:
        st.toast("Erro ao tentar fazer cadastro de novo usuário!", icon="❌")
        return False
    return True


def dict_edit_process(conn, cursor, process_path, case_value, def_case_value,
                      payed_value, judge_name, obs, process_number):


    register_process_dict = {
        'p_numero_processo': process_number,
        'p_caminho_processual': process_path,
        'p_valor_causa': case_value,
        'p_nome_juiz': judge_name,
        'p_valor_definido_causa': def_case_value,
        'p_valor_pago_causa': payed_value,
        'p_observacoes_clob': obs
    }
    send_values_edit_process(register_process_dict, conn, cursor)


def send_values_edit_process(register_process_dict, conn, cursor):
    sql = '''
    UPDATE processos_juridicos
    SET VALOR_CAUSA = :1,
        VALOR_DEFERIDO_CAUSA = :2
        VALOR_PAGO_CAUSA = :3,
        NOME_JUIZ = :4,
        OBSERVACOES_CLOB = :5,
        CAMINHO_PROCESSUAL = :6
    WHERE NUMERO_PROCESSO = :7
    '''