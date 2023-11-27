import pandas
import calplot

data = pandas.read_csv('pushup.csv', parse_dates=['date_time'])
data = data.set_index('date_time')
calplot.calplot(data['pushup'], cmap='YlGn', edgecolor='white')
