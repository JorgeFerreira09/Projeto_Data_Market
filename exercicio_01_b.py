import pandas as pd
import matplotlib as plt
import plotly.express as px

caminho_csv = "../dados/M07_P03_BASE_SUPERMERCADO.csv"

df = pd.read_csv(caminho_csv, encoding="utf-8")

pd.set_option("display.width", None)

categorias_traducao = {
    "belleza-y-cuidado-personal": "Beleza e Cuidado Pessoal",
    "congelados": "Congelados",
    "comidas-preparadas":"Comidas Prontas",
    "lacteos": "Lacteos",
    "instantaneos-y-sopas":"Instantaneos e Sopas",
    "frutas": "Frutas", 
    "verduras": "Verduras"
}

df["Categoria"] = df["Categoria"].map(categorias_traducao)

media_categoria = df.groupby("Categoria")["Preco_Normal"].mean().rename("Media")
mediana_categoria = df.groupby("Categoria")["Preco_Normal"].median().rename("Mediana")
df_resultado = pd.concat([media_categoria, mediana_categoria], axis=1)

media_maior_mediana = df_resultado[df_resultado["Media"] > df_resultado["Mediana"]]
media_menor_mediana = df_resultado[df_resultado["Mediana"] > df_resultado["Media"]]

print("\n", "Media > Mediana")
print(media_maior_mediana.map(lambda x: f"{x:.0f}"))

print("\n", "Media < Mediana")
print(media_menor_mediana.map(lambda x: f"{x:.0f}"))