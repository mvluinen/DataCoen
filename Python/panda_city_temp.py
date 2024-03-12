import pandas

data = pandas.read_csv('Datasets/city_temperature.csv')
data.drop(['State', 'Region'], axis=1, inplace=True)
data = data.drop(data[data['AvgTemperature'] == -99].index)
new_data = data.groupby(['City', 'Country'])['AvgTemperature'].mean()

print(new_data.tail(10))
print(data.tail(10))
# print(data.dtypes)
# print(new_data.info)
# print(data.describe())
