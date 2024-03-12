import pandas

data = pandas.read_csv('Datasets/water_quality.csv', delimiter=";")
data = data.drop([
    'Conductivity',
    'Organic_carbon',
    'Turbidity',
    'Potability',
    'Trihalomethanes',
    'Sulfate',
    'Hardness',
    'Solids',
    'Chloramines',
    'Region'], axis=1)

# data['ph'] = data['ph'].replace(".", ",")
print(data.info)
print(data.dtypes)
print(data.head(10))