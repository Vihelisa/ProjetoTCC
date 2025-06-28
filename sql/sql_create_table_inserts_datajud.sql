CREATE TABLE datajud_endpoints (
    justica VARCHAR2(100) NOT NULL,
    tribunal VARCHAR2(150) NOT NULL,
    endpoint VARCHAR2(500) NOT NULL
);

select * from datajud_endpoints;

-- Inserção de exemplos
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES
('Tribunais Superiores', 'Tribunal Superior do Trabalho', 'https://api-publica.datajud.cnj.jus.br/api_publica_tst/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES
('Tribunais Superiores', 'Tribunal Superior Eleitoral', 'https://api-publica.datajud.cnj.jus.br/api_publica_tse/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES
('Tribunais Superiores', 'Tribunal Superior de Justiça', 'https://api-publica.datajud.cnj.jus.br/api_publica_stj/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES
('Tribunais Superiores', 'Tribunal Superior Militar', 'https://api-publica.datajud.cnj.jus.br/api_publica_stm/_search');



INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES
('Justiça Federal', 'Tribunal Regional Federal da 1ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trf1/_search');

INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES
('Justiça Federal', 'Tribunal Regional Federal da 2ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trf2/_search');

INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES
('Justiça Federal', 'Tribunal Regional Federal da 3ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trf3/_search');

INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES
('Justiça Federal', 'Tribunal Regional Federal da 4ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trf4/_search');

INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES
('Justiça Federal', 'Tribunal Regional Federal da 5ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trf5/_search');

INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES
('Justiça Federal', 'Tribunal Regional Federal da 6ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trf6/_search');




INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'Tribunal de Justiça do Acre', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjac/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'Tribunal de Justiça de Alagoas', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjal/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'Tribunal de Justiça do Amazonas', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjam/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'Tribunal de Justiça do Amapá', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjap/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'Tribunal de Justiça da Bahia', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjba/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'Tribunal de Justiça do Ceará', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjce/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'TJ do Distrito Federal e Territórios', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjdft/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'Tribunal de Justiça do Espírito Santo', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjes/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'Tribunal de Justiça do Goiás', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjgo/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'Tribunal de Justiça do Maranhão', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjma/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'Tribunal de Justiça de Minas Gerais', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjmg/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'TJ do Mato Grosso de Sul', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjms/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'Tribunal de Justiça do Mato Grosso', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjmt/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'Tribunal de Justiça do Pará', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjpa/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'Tribunal de Justiça da Paraíba', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjpb/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'Tribunal de Justiça de Pernambuco', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjpe/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'Tribunal de Justiça do Piauí', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjpi/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'Tribunal de Justiça do Paraná', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjpr/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'Tribunal de Justiça do Rio de Janeiro', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjrj/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'TJ do Rio Grande do Norte', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjrn/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'Tribunal de Justiça de Rondônia', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjro/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'Tribunal de Justiça de Roraima', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjrr/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'Tribunal de Justiça do Rio Grande do Sul', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjrs/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'Tribunal de Justiça de Santa Catarina', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjsc/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'Tribunal de Justiça de Sergipe', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjse/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'Tribunal de Justiça de São Paulo', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjsp/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Estadual', 'Tribunal de Justiça do Tocantins', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjto/_search');



INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça do Trabalho', 'Tribunal Regional do Trabalho da 1ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trt1/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça do Trabalho', 'Tribunal Regional do Trabalho da 2ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trt2/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça do Trabalho', 'Tribunal Regional do Trabalho da 3ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trt3/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça do Trabalho', 'Tribunal Regional do Trabalho da 4ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trt4/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça do Trabalho', 'Tribunal Regional do Trabalho da 5ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trt5/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça do Trabalho', 'Tribunal Regional do Trabalho da 6ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trt6/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça do Trabalho', 'Tribunal Regional do Trabalho da 7ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trt7/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça do Trabalho', 'Tribunal Regional do Trabalho da 8ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trt8/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça do Trabalho', 'Tribunal Regional do Trabalho da 9ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trt9/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça do Trabalho', 'Tribunal Regional do Trabalho da 10ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trt10/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça do Trabalho', 'Tribunal Regional do Trabalho da 11ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trt11/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça do Trabalho', 'Tribunal Regional do Trabalho da 12ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trt12/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça do Trabalho', 'Tribunal Regional do Trabalho da 13ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trt13/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça do Trabalho', 'Tribunal Regional do Trabalho da 14ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trt14/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça do Trabalho', 'Tribunal Regional do Trabalho da 15ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trt15/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça do Trabalho', 'Tribunal Regional do Trabalho da 16ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trt16/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça do Trabalho', 'Tribunal Regional do Trabalho da 17ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trt17/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça do Trabalho', 'Tribunal Regional do Trabalho da 18ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trt18/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça do Trabalho', 'Tribunal Regional do Trabalho da 19ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trt19/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça do Trabalho', 'Tribunal Regional do Trabalho da 20ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trt20/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça do Trabalho', 'Tribunal Regional do Trabalho da 21ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trt21/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça do Trabalho', 'Tribunal Regional do Trabalho da 22ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trt22/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça do Trabalho', 'Tribunal Regional do Trabalho da 23ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trt23/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça do Trabalho', 'Tribunal Regional do Trabalho da 24ª Região', 'https://api-publica.datajud.cnj.jus.br/api_publica_trt24/_search');



INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal Regional Eleitoral do Acre', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-ac/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal Regional Eleitoral de Alagoas', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-al/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal Regional Eleitoral do Amazonas', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-am/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal Regional Eleitoral do Amapá', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-ap/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal de Justiça da Bahia', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-ba/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal Regional Eleitoral do Ceará', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-ce/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal Regional Eleitoral do Distrito Federal', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-dft/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal Regional Eleitoral do Espírito Santo', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-es/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal Regional Eleitoral do Goiás', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-go/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal Regional Eleitoral do Maranhão', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-ma/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal Regional Eleitoral de Minas Gerais', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-mg/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal Regional Eleitoral do Mato Grosso de Sul', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-ms/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal Regional Eleitoral do Mato Grosso', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-mt/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal Regional Eleitoral do Pará', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-pa/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal Regional Eleitoral da Paraíba', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-pb/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal Regional Eleitoral de Pernambuco', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-pe/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal Regional Eleitoral do Piauí', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-pi/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal Regional Eleitoral do Paraná', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-pr/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal Regional Eleitoral do Rio de Janeiro', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-rj/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal Regional Eleitoral do Rio Grande do Norte', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-rn/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal Regional Eleitoral de Rondônia', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-ro/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal Regional Eleitoral de Roraima', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-rr/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal Regional Eleitoral do Rio Grande do Sul', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-rs/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal Regional Eleitoral de Santa Catarina', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-sc/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal Regional Eleitoral de Sergipe', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-se/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal Regional Eleitoral de São Paulo', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-sp/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Eleitoral', 'Tribunal Regional Eleitoral do Tocantins', 'https://api-publica.datajud.cnj.jus.br/api_publica_tre-to/_search');



INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Militar', 'Tribunal Justiça Militar de Minas Gerais', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjmmg/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Militar', 'Tribunal Justiça Militar do Rio Grande do Sul', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjmrs/_search');
INSERT INTO datajud_endpoints (justica, tribunal, endpoint) VALUES ('Justiça Militar', 'Tribunal Justiça Militar de São Paulo', 'https://api-publica.datajud.cnj.jus.br/api_publica_tjmsp/_search');