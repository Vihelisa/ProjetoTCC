# JurisDash

O JurisDash é uma plataforma de visualização de dados jurídicos, desenvolvida com Python e Streamlit como Trabalho de Conclusão de Curso. A aplicação ajuda profissionais do direito a cadastrar, acompanhar e analisar processos judiciais, com indicadores financeiros e dashboards gerenciais.

## Acesse o projeto

**Aplicação online:** https://projetotcc-jurisdash.streamlit.app

Para testar com dados fictícios, use:

- **Usuário:** admin@gmail.com
- **Senha:** 1234

Os dados exibidos são fictícios e foram criados apenas para demonstração.

## Funcionalidades

- **Login, cadastro e recuperação de senha** de usuários.
- **Página inicial** com a apresentação do sistema.
- **Cadastro de processos jurídicos**, manual ou por consulta externa à API pública do DataJud (CNJ).
- **Histórico de processos**, com edição das informações cadastradas.
- **Área Financeira**, com resumo de valores em causa, deferidos e recebidos, evolução mensal, taxa de êxito por área e detalhamento por processo.
- **Dashboard gerencial**, com distribuição por área jurídica, etapas processuais, evolução temporal, magistrados, tribunais, probabilidade de êxito e mapas de calor.
- **Perfil do usuário**, com edição de dados pessoais.

## Tecnologias

- Python
- Streamlit
- pandas
- Plotly
- SQLite (banco de dados de teste)

## Executar localmente

Clone o repositório, instale as dependências e rode o app a partir da raiz do projeto:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Na primeira execução, o app cria o arquivo `data/app.db` e o preenche com os dados de teste. Para restaurar esses dados, apague esse arquivo e rode o app novamente.
