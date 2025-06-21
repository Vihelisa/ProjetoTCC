-- Criar tabela das classes de processos jurídicos 
CREATE TABLE classes_processo (
    classe_processo VARCHAR2(100) PRIMARY KEY
);

INSERT INTO classes_processo (classe_processo) VALUES ('Ação Trabalhista');
INSERT INTO classes_processo (classe_processo) VALUES ('Ação Civil');
INSERT INTO classes_processo (classe_processo) VALUES ('Ação Penal');
INSERT INTO classes_processo (classe_processo) VALUES ('Ação Tributária');
INSERT INTO classes_processo (classe_processo) VALUES ('Ação Administrativa');
INSERT INTO classes_processo (classe_processo) VALUES ('Ação Empresarial');
INSERT INTO classes_processo (classe_processo) VALUES ('Ação Constitucional');

select * from classes_processo



-- Criar tabela das classes de processos jurídicos 
CREATE TABLE caminho_processo (
    caminho_processual VARCHAR2(100) PRIMARY KEY
);
INSERT INTO caminho_processo (caminho_processual) VALUES ('Petição Inicial');
INSERT INTO caminho_processo (caminho_processual) VALUES ('Intimação');
INSERT INTO caminho_processo (caminho_processual) VALUES ('Contestação');
INSERT INTO caminho_processo (caminho_processual) VALUES ('Notificação');
INSERT INTO caminho_processo (caminho_processual) VALUES ('Conciliação');
INSERT INTO caminho_processo (caminho_processual) VALUES ('Sentença');
INSERT INTO caminho_processo (caminho_processual) VALUES ('Apelação');

select * from caminho_processo


-- Criar tabela dos dados do processo jurídico
