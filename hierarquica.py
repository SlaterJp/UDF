import plotly.express as px
import pandas as pd
estados = ['DF', 'GO', 'MS', 'MT',
    'AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE',
    'AC', 'AM', 'AP', 'PA', 'RO', 'RR', 'TO',
    'ES', 'MG', 'RJ', 'SP',
    'PR', 'RS', 'SC']
regioes =['Centro-Oeste', 'Centro-Oeste', 'Centro-Oeste', 'Centro-Oeste',
    'Nordeste', 'Nordeste', 'Nordeste', 'Nordeste', 'Nordeste', 'Nordeste', 'Nordeste', 'Nordeste', 'Nordeste',
    'Norte', 'Norte', 'Norte', 'Norte', 'Norte', 'Norte', 'Norte',
    'Sudeste', 'Sudeste', 'Sudeste', 'Sudeste',
    'Sul', 'Sul', 'Sul']
mortes = [12051, 28660, 11355, 15281,  # Centro-Oeste
    7380, 32147, 28215, 11109, 10748, 23302, 8449, 9354, 6592,  # Nordeste
    2118, 14556, 2178, 19343, 7527, 2200, 4322,  # Norte
    15259, 67205, 78473, 185212,  # Sudeste
    47082, 43258, 23250]
df = pd.DataFrame(dict(estados=estados,regioes=regioes,populacao=mortes))
df["all"] = "all" #garante um único nó raiz
fig = px.treemap(df,path=[regioes,estados],values=mortes,color='populacao',color_continuous_scale='YlOrRd', title='Visualização Hierárquica: Distribuição de Óbitos por COVID-19 no Brasil')
fig.show()

