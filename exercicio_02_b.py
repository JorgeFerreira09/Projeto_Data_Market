import pandas as pd
import matplotlib as plt
import plotly.express as px

caminho_csv = "../dados/M07_P03_BASE_SUPERMERCADO.csv"

df = pd.read_csv(caminho_csv, encoding="latin1")

pd.set_option("display.width", None)

categorias_traducao = {
    "belleza-y-cuidado-personal": "Beleza e Cuidado Pessoal",
    "congelados": "Congelados",
    "comidas-preparadas":"Comidas Prontas",
    "lacteos": "Lacteos",
    "instantaneos-y-sopas":"Instantâneos e Sopas",
    "frutas": "Frutas", 
    "verduras": "Verduras"
}

# Organização e Limpeza
df.rename(columns={"title":"Titulo"}, inplace=True)
df["Categoria"] = df["Categoria"].map(categorias_traducao)

media_por_categoria = df.groupby("Categoria")["Preco_Normal"].mean().rename("Media")
mediana_por_categoria = df.groupby("Categoria")["Preco_Normal"].median().rename("Mediana")

media_por_categoria = media_por_categoria.sort_values(ascending=False)
mediana_por_categoria = media_por_categoria.sort_values(ascending=False)

print("\n", media_por_categoria.apply(lambda x: f"{x:.0f}"))
print("\n", mediana_por_categoria.apply(lambda x: f"{x:.0f}"))