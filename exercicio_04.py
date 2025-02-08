import pandas as pd
import plotly.express as px

caminho_csv = "../dados/M07_P03_BASE_SUPERMERCADO.csv"

df = pd.read_csv(caminho_csv, encoding="latin1")

pd.set_option("display.width", None)

media_por_categoria = df.groupby("Categoria")["Desconto"].mean().reset_index()

categorias_traducao = {
    "belleza-y-cuidado-personal": "Beleza e Cuidado Pessoal",
    "congelados": "Congelados",
    "comidas-preparadas":"Comidas Prontas",
    "lacteos": "Lacteos",
    "instantaneos-y-sopas":"Instataneos e Sopas",,
    "frutas": "Frutas", 
    "verduras": "Verduras"
}

# Limpeza e Organização
media_por_categoria = (
    media_por_categoria
    .drop_duplicates()
    .sort_values(by="Desconto", ascending=False)
    .round(0)
)

media_por_categoria["Categoria"] = media_por_categoria["Categoria"].map(categorias_traducao)
print(media_por_categoria)

fig = px.bar (
        media_por_categoria,
        y = "Desconto",
        x = "Categoria",
        title = "Desconto Médio por Categoria",
        labels={"Desconto": "Desconto ($)"},
        text_auto=True,
    )

fig.update_traces(
        marker_color="#554c66",         # Lílas Escuro
        marker_line_width=1.5,
        marker_line_color='#cbbce6',    # Lílas Claro
        opacity=0.8,
        textfont=dict(color="black", size=14),
        textposition="outside"
)

fig.update_layout(
        title_font_size=18,
        title_font_color="black",
        height=700,        
        width=1200,
        xaxis_title='',
        xaxis_tickfont=dict(size=14, color="black"),
        yaxis_title_font_size=16, 
        yaxis_title_font_color="Black",
        yaxis=dict(
            showticklabels=False,
            tickfont=dict(size=14)
        ),
    )

fig.show()