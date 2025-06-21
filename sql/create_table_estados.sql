-- Criando tabela para ser lista de estados do brasil
CREATE TABLE estados_brasil (
    nome_estado VARCHAR2(50) NOT NULL,
    sigla_estado VARCHAR2(2) NOT NULL,
    CONSTRAINT pk_estado PRIMARY KEY (sigla_estado)
);

INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('Acre', 'AC');
INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('Alagoas', 'AL');
INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('Amapá', 'AP');
INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('Amazonas', 'AM');
INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('Bahia', 'BA');
INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('Ceará', 'CE');
INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('Distrito Federal', 'DF');
INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('Espírito Santo', 'ES');
INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('Goiás', 'GO');
INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('Maranhão', 'MA');
INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('Mato Grosso', 'MT');
INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('Mato Grosso do Sul', 'MS');
INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('Minas Gerais', 'MG');
INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('Pará', 'PA');
INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('Paraíba', 'PB');
INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('Paraná', 'PR');
INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('Pernambuco', 'PE');
INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('Piauí', 'PI');
INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('Rio de Janeiro', 'RJ');
INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('Rio Grande do Norte', 'RN');
INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('Rio Grande do Sul', 'RS');
INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('Rondônia', 'RO');
INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('Roraima', 'RR');
INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('Santa Catarina', 'SC');
INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('São Paulo', 'SP');
INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('Sergipe', 'SE');
INSERT INTO estados_brasil (nome_estado, sigla_estado) VALUES ('Tocantins', 'TO');

select * from estados_brasil;
