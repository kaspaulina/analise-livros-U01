import numpy as np
import pandas as pd
import streamlit as st
from streamlit_card import card
from streamlit_extras.dataframe_explorer import dataframe_explorer

st.title("Análise dos dados do aplicativo Skoob")
st.markdown("Dados disponíveis em: https://www.kaggle.com/datasets/victorstein/livros-skoob")

st.divider()

st.header("Sobre os dados")
st.write("Skoob é uma plataforma digital e aplicativo sobre leituras. O usuário pode pesquisar sobre livros, registrar suas leituras e avaliá-las. Este trabalho analisa uma amostra do dataset.")
st.write("Quantidade de linhas da amostra: 2500. Originalmente havia quase 12 mil linhas")
st.write("Colunas: titulo, autor, ano, paginas, rating, avaliacao, resenha, abandonos, relendo, lendo, querem_ler, leram, genero, male, female.")

st.subheader("Explore os dados")
st.write("Você pode selecionar uma ou mais colunas para filtrar abaixo:") 
df = pd.read_csv("./livros-skoob-sample.csv")
filter_df = dataframe_explorer(df)
st.dataframe(filter_df[["titulo", "autor", "ano", "paginas", "editora", "rating", "avaliacao", "resenha", "abandonos", "relendo", "lendo", "querem_ler", "leram", "genero", "male", "female"]])

st.subheader("Estatísticas")
#variaveis
media_paginas = np.mean(df.paginas).round()
media_rating = np.mean(df.rating).round()
quant_editoras = len(set(df.editora))
quant_livros = len(df)
#fim varivaeis

#cards
col1, col2, col3 = st.columns(3,gap="small")

with col1:
    quant_livros = card(
    title=str(quant_livros),
    text="Livros",
    styles={
      "card": {
        "width": "180px",
        "height": "180px",
        "padding": "0px",
        "background-image": "linear-gradient(to right top, #051937, #00456b, #007899, #00adbd, #47e4d4)"
        }
    }
)

with col2:
    quant_editoras_card = card(
    title=str(quant_editoras),
    text="Editoras",
    styles={
      "card": {
        "width": "180px",
        "height": "180px",
        "padding": "0",
        "background-image": "linear-gradient(to right top, #051937, #00456b, #007899, #00adbd, #47e4d4)"
        }
    }
)

with col3:
    media_paginas_card = card(
    title=str(media_paginas),
    text="Média de Páginas",
    styles={
      "card": {
        "width": "180px",
        "height": "180px",
        "padding": "0",
        "background-image": "linear-gradient(to right top, #051937, #00456b, #007899, #00adbd, #47e4d4)"
       }
    }
)


st.divider()

st.header("Leituras")
st.write("O skoob possui 4 status: abandonei, relendo, lendo, quero ler e lido.")
# top 5 mais lidos (gráfico de barra ou gráfico de linha ou dataframe/tabela)
# top 5 mais abandonados (gráfico de barra ou gráfico de linha ou dataframe/tabela) 
# top 5 mais desejados (status quero ler) (gráfico de barra ou gráfico de linha ou dataframe/tabela)

st.divider()

st.header("Notas")
st.write("Os usuários do Skoob podem avaliar suas leituras em notas de 0 a 5, sendo 5 'Perfeito'.")
# informar média das notas no texto ou dispor em um card
# histograma do rating
# livros mais avaliados (rating maior que 4.5 até 5.0) (dataframe/tabela)
# top 5 ou 10 menos avaliados (gráfico de linha ou dataframe/tabela)

st.divider()

st.header("Edição dos Livros")
st.write("Mais informações sobre os livros do dataset.")

# quantidade de livros por editora (gráfico de barra ou de linha)
# quantidade de livros por ano (gráfico de barra ou de linha)
# histograma da quantidade de páginas dos livros

st.divider()
st.text("Unidade 01 - Sistemas de Apoio à Decisão")
st.text("Grupo: AMANDA LIMA DA SILVA, BRENO GABRIEL DA SILVA SACERDOTE, DIEGO GOMES DE SANTANA, PAULINA KAYSE DE ANDRADE SANTOS.")