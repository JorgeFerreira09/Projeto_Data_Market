import pandas as pd
import plotly.express as px

df = pd.read_csv("M07_P03_BASE_SUPERMERCADO.csv", encoding="latin1")

pd.set_option("display.width", None)

traducao_categorias = {
    "belleza-y-cuidado-personal": "Beleza e Cuidado Pessoal",
    "congelados": "Congelados",
    "comidas-preparadas":"Comidas Prontas",
    "lacteos": "Lacteos",
    "instantaneos-y-sopas":"Instantâneos e Sopas",
    "frutas": "Frutas", 
    "verduras": "Verduras"
}

media_por_categoria_marca = df.groupby(["Categoria", "Marca"])["Desconto"].mean().reset_index()

media_por_categoria_marca["Categoria"] = media_por_categoria_marca["Categoria"].map(traducao_categorias)

fig = px.treemap(
        media_por_categoria_marca.round(0),
        path=["Categoria", "Marca"],
        values="Desconto",
        title="Desconto Médio Por Categoria e Marca: "
)       

fig.update_layout(
        width=1280,
        margin=dict(l=50, r=50, b=50, t=50)
)

fig.show()
