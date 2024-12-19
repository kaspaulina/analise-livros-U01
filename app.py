import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
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

with st.expander("Top 5 Livros mais lidos"):
  mais_lidos = df[df['leram'] > 0].sort_values(by='leram', ascending=False).head(5)
  st.dataframe(mais_lidos[['titulo', 'rating', 'avaliacao','leram']])

# top 5 mais abandonados (gráfico de barra ou gráfico de linha ou dataframe/tabela) 
with st.expander("Top 5 Livros mais abandonados"):
    mais_abandonados = df[df['abandonos'] > 0].sort_values(by='abandonos', ascending=False).head(5)
    st.dataframe(mais_abandonados[['titulo', 'rating', 'avaliacao','abandonos','ano','paginas']])

# top 5 mais desejados (status quero ler) (gráfico de barra ou gráfico de linha ou dataframe/tabela)
with st.expander("Top 5 Livros mais Desejados"):
    mais_desejados = df[df['querem_ler'] > 0].sort_values(by='querem_ler', ascending=False).head(5)
    plt.figure(figsize=(15, 10))
    bars = plt.bar(mais_desejados['titulo'], mais_desejados['querem_ler'], color='skyblue')
    plt.bar_label(bars, fmt='%d', padding=5)
    plt.xlabel('Título do Livro')
    plt.ylabel('Quantidade de Pessoas Querendo Ler')
    plt.title('Top 5 Livros Mais Desejados')

    st.pyplot(plt)

st.divider()

st.header("Notas")
st.write("Os usuários do Skoob podem avaliar suas leituras em notas de 0 a 5, sendo 5 'Perfeito'.")
# informar média das notas no texto ou dispor em um card
# histograma do rating
# livros mais avaliados (rating maior que 4.5 até 5.0) (dataframe/tabela)
# top 5 ou 10 menos avaliados (gráfico de linha ou dataframe/tabela)
with st.expander("Distribuição das Notas"):
    plt.figure(figsize=(10, 6))
    plt.hist(df['rating'], bins=np.arange(0, 6, 0.5), edgecolor='black', alpha=0.7)
    plt.title("Histograma das Notas ")
    plt.xlabel("Notas")
    plt.ylabel("Quantidade de Livros")
    plt.xticks(np.arange(0, 6, 0.5))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(plt)

with st.expander("Livros Mais Bem Avaliados (Rating > 4.5)"):
    mais_avaliados = df[(df['rating'] > 4.5) & (df['rating'] <= 5.0)]
    mais_avaliados = mais_avaliados[['titulo', 'rating', 'avaliacao']].sort_values(by='rating', ascending=False)
    st.dataframe(mais_avaliados)

with st.expander("Top 10 Livros Menos Bem Avaliados"):
    menos_avaliados = df[df['avaliacao'] > 0].sort_values(by='rating', ascending=True).head(10)
    st.dataframe(menos_avaliados[['titulo', 'rating', 'avaliacao']])


# Edição dos Livros
st.divider()

st.header("Edição dos Livros")
st.write("Mais informações sobre os livros do dataset.")

with st.expander("Top 10 Editoras com Mais Livros"):
    # Quantidade de livros por editora
    quant_livros_editora = df['editora'].value_counts()
    plt.figure(figsize=(10, 6))

    # Gráfico de Barras
    ax = quant_livros_editora.head(10).plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title("Top 10 Editoras com Mais Livros")
    plt.xlabel("Editora")
    plt.ylabel("Quantidade de Livros")

    # Alinhamento de títulos na barra
    plt.xticks(rotation=0, ha='center', fontsize=10)

    # Adicionando a grade
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Adicionando os valores nas barras
    for i in ax.patches:
        ax.text(i.get_x() + i.get_width() / 2, i.get_height() + 0.05,
                str(int(i.get_height())), 
                ha='center', va='bottom', fontweight='bold', fontsize=10)

    # Exibe o gráfico
    st.pyplot(plt)

with st.expander("Quantidade de livros lançados por ano (últimos 10 anos)"):
    # Filtra os dados para pegar apenas os últimos 10 anos
    anos_mais_recentes = sorted(df['ano'].unique())[-10:]
    df_ultimos_10_anos = df[df['ano'].isin(anos_mais_recentes)]
    quant_livros_ano = df_ultimos_10_anos['ano'].value_counts().sort_index()

    plt.figure(figsize=(10, 6))
    ax = quant_livros_ano.plot(kind='bar', color='lightgreen', edgecolor='black')
    plt.title("Quantidade de Livros Lançados nos Últimos 10 Anos")
    plt.xlabel("Ano")
    plt.ylabel("Quantidade de Livros")
    plt.xticks(rotation=0, ha='center', fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    for i in ax.patches:
        ax.text(i.get_x() + i.get_width() / 2, i.get_height() + 0.05,
                str(int(i.get_height())),
                ha='center', va='bottom', fontweight='bold', fontsize=10)

    st.pyplot(plt)

with st.expander("Top 10 Editoras Mais Lidas"):
    livros_leram = df[df['leram'] > 0]
    livros_abandonados = df[df['abandonos'] > 0]
    top_10_editoras_lidos = livros_leram['editora'].value_counts().head(10)
    
    # Lista para armazenar as informações sobre editoras
    editoras_info = []
    for editora in top_10_editoras_lidos.index:
        livros_editora_lidos = livros_leram[livros_leram['editora'] == editora]
        livros_editora_abandonados = livros_abandonados[livros_abandonados['editora'] == editora]
        livros_editora_lidos_count = livros_editora_lidos.groupby('titulo')['leram'].sum().sort_values(ascending=False)
        # O livro mais lido
        livro_mais_lido = livros_editora_lidos_count.idxmax()
        livros_editora_abandonados_count = livros_editora_abandonados.groupby('titulo')['abandonos'].sum().sort_values(ascending=False)
        # O livro mais abandonado
        livro_mais_abandonado = livros_editora_abandonados_count.idxmax() if not livros_editora_abandonados_count.empty else 'Nenhum Abandonado'
        #Colunas
        editoras_info.append([editora, livro_mais_lido, livro_mais_abandonado])
    #tabela
    top_10_editoras_lidos_df = pd.DataFrame(editoras_info, columns=['Editora', 'Livro Mais Lido', 'Livro Mais Abandonado'])
    top_10_editoras_lidos_df.index = top_10_editoras_lidos_df.index + 1
    st.dataframe(top_10_editoras_lidos_df)
st.divider()
st.text("Unidade 01 - Sistemas de Apoio à Decisão")
st.text("Grupo: AMANDA LIMA DA SILVA, BRENO GABRIEL DA SILVA SACERDOTE, DIEGO GOMES DE SANTANA, PAULINA KAYSE DE ANDRADE SANTOS.")