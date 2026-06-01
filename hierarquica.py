import plotly.express as px
import pandas as pd

continentes = [
    'Américas', 'Américas', 'Américas', 'Américas',
    'Europa', 'Europa', 'Europa', 'Europa',
    'Mediterrâneo Oriental', 'Mediterrâneo Oriental', 'Mediterrâneo Oriental', 'Mediterrâneo Oriental',
    'Pacífico Ocidental', 'Pacífico Ocidental', 'Pacífico Ocidental', 'Pacífico Ocidental',
    'Sudeste Asiático', 'Sudeste Asiático', 'Sudeste Asiático', 'Sudeste Asiático',
    'África', 'África', 'África', 'África'
]

paises = [
    'United States', 'Brazil', 'Argentina', 'Mexico',                     # Américas
    'France', 'Germany', 'Italy', 'United Kingdom',                        # Europa
    'Iran', 'Iraq', 'Jordan', 'Pakistan',                                  # Mediterrâneo Oriental
    'China', 'South Korea', 'Japan', 'Australia',                          # Pacífico Ocidental
    'India', 'Thailand', 'Bangladesh', 'Nepal',                            # Sudeste Asiático
    'South Africa', 'Ethiopia', 'Réunion', 'Zambia'                        # África
]

casos_acumulados = [
    103436829, 38021677, 10119347, 7630026,                                # Américas
    39060446, 38437953, 26969913, 25117472,                                # Europa
    7627863, 2465545, 1746997, 1580631,                                    # Mediterrâneo Oriental
    99381761, 34571873, 33803572, 11861161,                                # Pacífico Ocidental
    45056221, 5427969, 2052280, 1003968,                                   # Sudeste Asiático
    4073188, 501339, 494595, 349892                                        # África
]

df = pd.DataFrame(dict(paises=paises, continentes=continentes, casos=casos_acumulados))
df["all"] = "all"

fig = px.treemap(
    df,
    path=[continentes, paises],
    values=casos_acumulados,
    color='casos',
    color_continuous_scale='YlOrRd',
    title='Visualização Hierárquica: Top 4 Países com Mais Casos de COVID-19 por Continente'
)

fig.show()