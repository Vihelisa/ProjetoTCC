--Procedure 
CREATE OR REPLACE PROCEDURE inserir_processo_com_arquivo (
    p_numero_processo        IN VARCHAR2,
    p_classe_processo        IN VARCHAR2,
    p_rito_processo          IN VARCHAR2,
    p_nome_advogado          IN VARCHAR2,
    p_numero_oab             IN VARCHAR2,
    p_nome_cliente_empresa   IN VARCHAR2,
    p_caminho_processual     IN VARCHAR2,
    p_nome_juiz              IN VARCHAR2,
    p_estado_processo        IN CHAR,
    p_valor_causa            IN NUMBER,
    p_valor_definido_causa   IN NUMBER,
    p_valor_pago_causa       IN NUMBER,
    p_observacoes_clob       IN CLOB,
    p_nome_arquivo           IN VARCHAR2,
    p_arquivo_pdf            IN BLOB,
    p_justica                IN VARCHAR2,
    p_tribunal               IN VARCHAR2
)
AS
BEGIN
    -- Inserção na tabela principal
    INSERT INTO processos_juridicos (
        numero_processo, classe_processo, rito_processo, nome_advogado,
        numero_oab, nome_cliente_empresa, caminho_processual, nome_juiz,
        estado_processo, valor_causa, valor_deferido_causa, valor_pago_causa,
        observacoes_clob, justica, tribunal
    ) VALUES (
        p_numero_processo, p_classe_processo, p_rito_processo, p_nome_advogado,
        p_numero_oab, p_nome_cliente_empresa, p_caminho_processual, p_nome_juiz,
        p_estado_processo, p_valor_causa, p_valor_definido_causa, p_valor_pago_causa,
        p_observacoes_clob, p_justica, p_tribunal
    );

    -- Inserção na tabela de arquivos
    INSERT INTO arquivos_processos (
        numero_processo, nome_arquivo, arquivo_pdf
    ) VALUES (
        p_numero_processo, p_nome_arquivo, p_arquivo_pdf
    );

    COMMIT;
END;