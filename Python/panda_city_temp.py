import pandas
import plotly.express as px


def city_temp():
    data = pandas.read_csv('Datasets/city_temperature.csv')
    data.drop(['State', 'Region'], axis=1, inplace=True)
    data = data.drop(data[data['AvgTemperature'] == -99].index)
    new_data = data.groupby(['City', 'Country'])['AvgTemperature'].mean()
    # print(new_data.tail(10))

    return new_data
    # print(data.tail(10))
    # print(data.dtypes)
    # print(new_data.info)
    # print(data.describe())


def water():
    dataw = pandas.read_csv('Datasets/water_quality.csv', delimiter=";")
    dataw = dataw.drop([
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
    dataw['WaterPollution'].fillna(0, inplace=True)
    for i in range(0, len(dataw)):
        dataw.at[i, 'WaterPollution'] = int(str(dataw['WaterPollution'][i]).replace('.', ''))
    return dataw


def merge_it():
    final_df = pandas.merge(city_temp(), water(), how='right', on='City')
    print(final_df.tail(10))
    return final_df


def correlation(final_df):
    print(final_df['AvgTemperature'].corr(final_df['WaterPollution']))


def plot(final_df):
    fig = px.scatter(final_df, x='AvgTemperature', y='WaterPollution')
    fig.show()


if __name__ == '__main__':
    df = merge_it()
    correlation(final_df=df)
    plot(final_df=df)
