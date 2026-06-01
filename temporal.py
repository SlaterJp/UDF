from google.colab import drive
drive.mount('/content/drive')
from pandas import read_csv
from matplotlib import pyplot

# Carrega o arquivo do seu link do Drive e processa os dados em uma única linha
series = read_csv(r"/content/drive/MyDrive/caso_full.csv.gz", index_col='date', parse_dates=True).query("place_type == 'state'").groupby('date')['new_confirmed'].sum()

series.plot() 
pyplot.show()