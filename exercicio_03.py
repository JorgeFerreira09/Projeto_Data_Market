import pandas as pd
import matplotlib as plt
import plotly.express as px

#   Caminho do arquivo csv
caminho_csv = "../dados/M07_P03_BASE_SUPERMERCADO.csv"

df = pd.read_csv(caminho_csv, encoding="utf-8")

df_lacteos = df.loc[df["Categoria"] == 'lacteos',["Preco_Normal"]]

# Organização e Limpeza
df_lacteos = df_lacteos.dropna()
df_lacteos = df_lacteos.drop_duplicates()                                         
valores_negativos = df_lacteos.loc[df_lacteos["Preco_Normal"] < 0]    
print(" Valores Negativos: Inexistentes. " if valores_negativos.empty else valores_negativos, "\n")

# Gráfico
fig = px.box(
    df_lacteos,
    y="Preco_Normal",
    title="Boxplot Preco Normal da Categoria Lacteos",
    width=720,
    height=680,
    color_discrete_sequence=["purple"],
    labels={"Preco_Normal": "Preço Normal ($) "},
    points="all"
)

fig.show()
  

# BoxSplot
q1, mediana, q3 = df_lacteos["Preco_Normal"].quantile([0.25, 0.50, 0.75]) 
iqr = q3-q1
limite_superior = q3 + 1.5 * iqr
limite_inferior = q1 - 1.5 * iqr

outliers_unicos_cima = df_lacteos[df_lacteos["Preco_Normal"] > limite_superior].drop_duplicates().shape[0]
outliers_unicos_baixo = df_lacteos[df_lacteos["Preco_Normal"] < limite_inferior].drop_duplicates().shape[0]

print("Boxplot Medidas Importantes: ", "\n")
print("Qtd de Outliers Unicos Acima do Limite Superior: ", outliers_unicos_cima)
print("Qtd de Outliers Unicos Abaixo do Limite Inferior: ", outliers_unicos_baixo)
print("\n")
print(f"Primeiro Quartil (Q1): {q1:.0f}") 
print(f"Terceiro Quartil (Q3): {q3:.0f}")
print(f"Mediana: {mediana:.0f}")
print(f"IQR: {iqr:.0f}")
print("\n")
print(f"Limite Superior: {limite_superior:.0f}")
print("Limite Inferior: ", limite_inferior)
