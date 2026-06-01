from pandas import read_csv
from matplotlib import pyplot

url = "https://raw.githubusercontent.com/SlaterJp/UDF/main/caso_full.csv.gz"

series = (
    read_csv(
        url,
        index_col='date',
        parse_dates=True,
        compression='gzip'
    )
    .query("place_type == 'state'")
    .groupby('date')['new_confirmed']
    .sum()
)

series.plot()
pyplot.show()