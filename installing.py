'''Week 12 Team Activity'''
import pandas
from datetime import datetime
data = pandas.read_csv("weather_year.csv")
print(data)
print(len(data))
print(data.columns)
print(data['EDT'])  # same output
print(data[['EDT', 'Mean TemperatureF']])
print(data.EDT)  # same output
print(data.EDT.head())  # tail() last rows.
print(data.EDT.head(10))
print(data["Mean TemperatureF"].head())

'''Fun with columns'''
data.columns = ["date", "max_temp", "mean_temp", "min_temp", "max_dew",
                "mean_dew", "min_dew", "max_humidity", "mean_humidity",
                "min_humidity", "max_pressure", "mean_pressure",
                "min_pressure", "max_visibilty", "mean_visibility",
                "min_visibility", "max_wind", "mean_wind", "min_wind",
                "precipitation", "cloud_cover", "events", "wind_dir"]

print(data)
print(data.mean_temp.head())
print(data.mean_temp.std())
print(data.mean_temp.hist())
print(data.std())

'''Bulk operations with apply()'''

print(data.date.head())
first_date = data.date.values[0]
print(first_date)
print(datetime.strptime(first_date, "%Y-%m-%d"))
data.date = data.date.apply(lambda d: datetime.strptime(d, "%Y-%m-%d"))
print(data.date.head())
data.index = data.date
print(data)
# print(data.ix[datetime(2012, 8, 19)]) # no working because of ix
data = data.drop(["date"], axis=1)
print(data.columns)

'''Handling missing values'''
empty = data.apply(lambda col: pandas.isnull(col))
print(empty)
print(empty.events.head(10))
print(data.events.head(10))
print(data.dropna(subset=["events"]))
data.events = data.events.fillna("")
print(data.events.head(10))

'''Accesing individual rows'''
print(data.iloc[0])
# print(data.ix[datetime(2013, 1, 1)]) because of ix
num_rain = 0
for idx, row in data.iterrows():
    if "Rain" in row["events"]:
        num_rain += 1

print("Days with rain: {0}".format(num_rain))
