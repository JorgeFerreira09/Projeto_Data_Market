import pandas as pd
import matplotlib as plt
import plotly.express as px

caminho_csv = "../dados/M07_P03_BASE_SUPERMERCADO.csv"

df = pd.read_csv(caminho_csv, encoding="utf-8")

pd.set_option("display.width", None)

df.rename(columns={"title":"Titulo"}, inplace=True)

media_por_categoria = df.groupby("Categoria")["Preco_Normal"].mean().rename("Media", inplace=True)
mediana_por_categoria = df.groupby("Categoria")["Preco_Normal"].median().rename("Mediana", inplace=True)

media_por_categoria = media_por_categoria.sort_values(ascending=False)
mediana_por_categoria = media_por_categoria.sort_values(ascending=False)

print("\n", media_por_categoria.apply(lambda x: f"{x:.0f}"))
print("\n", mediana_por_categoria.apply(lambda x: f"{x:.0f}"))