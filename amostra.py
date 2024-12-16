import pandas as pd
import numpy as np

data = pd.read_csv("./dados.csv")
select_data = data[["titulo", "autor", "ano", "paginas", "editora","rating", "avaliacao", "resenha", "abandonos", "relendo", "lendo", "querem_ler", "leram", "genero", "male", "female"]]
select_data.loc[select_data.genero=="", 'genero'] = np.nan
select_data.loc[select_data.genero==" ", 'genero'] = np.nan
select_data.loc[select_data.genero=="  ", 'genero'] = np.nan
select_data_filter = select_data.dropna()
amostra = select_data_filter.sample(n=2500)

amostra.to_csv("./livros-skoob-sample.csv", index=False)
