from pandas import read_csv
from matplotlib import pyplot

url = "https://raw.githubusercontent.com/SlaterJp/UDF/main/WHO-COVID-19-global-daily-data.csv"

df = read_csv(url, parse_dates=['Date_reported'])

df.set_index('Date_reported', inplace=True)

series_mensal = df['New_cases'].resample('ME').sum()

series_mensal.plot(figsize=(12, 6), marker='o', color='#1f77b4', linewidth=2)

pyplot.title("Evolução Temporal: Total de Novos Casos Globais de COVID-19 por Mês")
pyplot.xlabel("Intervalo Temporal (Ano-Mês)")
pyplot.ylabel("Total de Casos no Mês")
pyplot.grid(True, linestyle='--', alpha=0.5)

pyplot.show()