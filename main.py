import pandas
import calplot

data = pandas.read_csv('pushup.csv', parse_dates=['date_time'])
data = data.set_index('date_time')
print(data)
fig, ax = calplot.calplot(data['pushup'], cmap='YlGn', edgecolor='white', figsize=(12, 3.8))
fig.savefig('result.png')
