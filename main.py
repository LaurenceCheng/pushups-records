import pandas
import calplot

data = pandas.read_csv('pushup.csv', parse_dates=['date_time'])
data = data.set_index('date_time')
print(data)
fig, ax = calplot.calplot(data['pushup'], cmap='YlGn', edgecolor='white', vmax=40.0)
fig.savefig('result.png')
