import pandas as pd
import matplotlib as plt
import plotly.express as px

caminho_csv = "../dados/M07_P03_BASE_SUPERMERCADO.csv"

df = pd.read_csv(caminho_csv, encoding="latin1")

pd.set_option("display.width", None)

df.rename(columns={"title":"Titulo"}, inplace=True)

print(df.head())

desvio_padrao = df.groupby("Categoria")["Preco_Normal"].std().round(2).rename("Desvio_Padrao", inplace=True)

print("\n", desvio_padrao)
