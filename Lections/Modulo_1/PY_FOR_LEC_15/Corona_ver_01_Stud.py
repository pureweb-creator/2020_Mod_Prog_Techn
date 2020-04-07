# -*- coding: utf-8 -*-
"""
Created on Mon Apr 5 2020

@author: eab19

ОЦЕНКА ПИКА и ДЛИТЕЛЬНОСТИ ЭПИДЕМИИ

Описание  и  скрипты смотри
https://habr.com/ru/post/495752/

Данные от
https://systems.jhu.edu/research/public-health/ncov/

"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import timedelta, datetime

# График по конкретной стране с прогнозом
def plot_by_country(country):
    '''
    Parameters
    ----------
    country : str
        DESCRIPTION.  country name

    Returns
    -------
    None.

    '''
    # Формируем надписи легенды
    l1 = 'Infected at ' + last_date + ' - ' + str(confirmed.loc[confirmed['Country/Region'] == country,:].sum()[-1])
    l2 = 'Recovered at ' + last_date + ' - ' + str(recovered.loc[recovered['Country/Region'] == country,:].sum()[-1])
    l3 = 'Dead at ' + last_date + ' - ' + str(deaths.loc[deaths['Country/Region'] == country,:].sum()[-1])

    # Формируем pandas датафрейм с данными по выбранной стране
    df = pd.DataFrame(confirmed_daily.loc[confirmed_daily['Country/Region'] == country,:].sum()[4:])
    df.columns = ['confirmed_daily']
    df['recovered_daily'] = recovered_daily.loc[recovered_daily['Country/Region'] == country,:].sum()[4:]
    df['deaths_daily'] = deaths_daily.loc[deaths_daily['Country/Region'] == country,:].sum()[4:]
    df['deaths_daily'] = deaths_daily.loc[deaths_daily['Country/Region'] == country,:].sum()[4:]
    df['smooth_conf_daily'] = smooth_conf_daily.loc[smooth_conf_daily['Country/Region'] == country,:].sum()[4:]

    # Рисуем график
    fig, ax = plt.subplots(figsize = [16,6], nrows = 1)
    plt.title('COVID-19 dinamics daily in ' + country)

    # Наносим ежедные цифры по приросту заразившихся, выздоровевших и погибших
    ax.bar(df.index, df.confirmed_daily, alpha = 0.5, color = 'orange', label = l1)
    ax.bar(df.index, df.recovered_daily, alpha = 0.6, color = 'green', label = l2)
    ax.bar(df.index, df.deaths_daily, alpha = 0.7, color = 'red', label = l3)
    ax.plot(df.index, df.smooth_conf_daily, alpha = 0.7, color = 'black')

    # Наносим даты начала и пика.
    start_date = confirmed_top[confirmed_top.index == country].start_date.iloc[0]
    start_point = smooth_conf_daily.loc[smooth_conf_daily['Country/Region'] == country, start_date].sum()
    ax.plot_date(start_date, start_point, 'o', alpha = 0.7, color = 'black')
    shift = confirmed_top.loc[confirmed_top.index == country, 'trend_max'].iloc[0]/40
    plt.text(start_date, start_point + shift, 'Start at ' + start_date, ha ='right', fontsize = 20)

    peak_date = confirmed_top[confirmed_top.index == country].peak_date.iloc[0]
    peak_point = smooth_conf_daily.loc[smooth_conf_daily['Country/Region'] == country, peak_date].sum()
    ax.plot_date(peak_date, peak_point, 'o', alpha = 0.7, color = 'black')
    plt.text(peak_date, peak_point + shift, 'Peak at ' + peak_date, ha ='right', fontsize = 20)

    ax.xaxis.grid(False)
    ax.yaxis.grid(False)
    ax.tick_params(axis = 'x', labelrotation = 90)
    ax.legend(loc = 'upper left', prop=dict(size=12))

    # Выводим название страны крупно и прогнозную дата спада эпидемии.
    max_pos = max(df['confirmed_daily'].max(), df['recovered_daily'].max())
    if confirmed_top[confirmed_top.index == country].peak_passed.iloc[0]:
        estimation = 'peak is passed - end of infection ' + confirmed_top[confirmed_top.index == country].end_date.iloc[0]
    else:
        estimation = 'peak is not passed - end of infection is not clear'
    plt.text(df.index[len(df.index)//2], 3*max_pos//4, country, ha ='center', fontsize = 50)
    plt.text(df.index[len(df.index)//2], 2*max_pos//3, estimation, ha ='center', fontsize = 20)

    #plt.savefig(country + '.png', bbox_inches='tight', dpi = 75)
    plt.show()

#-----------------------------------------------------------
#                             M A I N
#-----------------------------------------------------------
pd.set_option('display.max_columns', None)

# Загружаем данные  в CSV формате
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'
confirmed = pd.read_csv(url + 'time_series_covid19_confirmed_global.csv', sep = ',')
deaths = pd.read_csv(url + 'time_series_covid19_deaths_global.csv', sep = ',')
recovered = pd.read_csv(url + 'time_series_covid19_recovered_global.csv', sep = ',')


# Преобразуем даты в формат 'dd.mm.yy'
new_cols = list(confirmed.columns[:4]) + list(confirmed.columns[4:].map(lambda x: '{0:02d}.{1:02d}.{2:d}'.format(int(x.split(sep='/')[1]), int(x.split(sep='/')[0]), int(x.split(sep='/')[2]))))
confirmed.columns = new_cols
recovered.columns = new_cols
deaths.columns = new_cols

# Формируем таблицы с ежедневными приращениями
confirmed_daily = confirmed.copy()
confirmed_daily.iloc[:,4:] = confirmed_daily.iloc[:,4:].diff(axis=1)
deaths_daily = deaths.copy()
deaths_daily.iloc[:,4:] = deaths_daily.iloc[:,4:].diff(axis=1)
recovered_daily = recovered.copy()
recovered_daily.iloc[:,4:] = recovered_daily.iloc[:,4:].diff(axis=1)

# Формируем таблицу со сглаженными (усредняющий фильтр) ежедневными приращениями заболевших
smooth_conf_daily = confirmed_daily.copy()
smooth_conf_daily.iloc[:,4:] = smooth_conf_daily.iloc[:,4:].rolling(window=8, min_periods=2, center=True, axis=1).mean()
smooth_conf_daily.iloc[:,4:] = smooth_conf_daily.iloc[:,4:].round(1)

# Определяем последнюю дату, на которую есть данные
last_date = confirmed.columns[-1]

# Определяем 20 стран с максимальным количеством подтвержденных случаев заражения
confirmed_top = confirmed.iloc[:, [1, -1]].groupby('Country/Region').sum().sort_values(last_date, ascending = False).head(20)
countries = list(confirmed_top.index)

# Определяем, какую долю зараженных дают эти 20 стран
conf_tot_ratio = confirmed_top.sum() / confirmed.iloc[:, 4:].sum()[-1]

# Добавляем к списку Украину
countries.append('Ukraine')


# Формируем легенду с колчеством подтвержденных случаев зараженных, вылечившихся и умерших
l1 = 'Infected at ' + last_date + ' - ' + str(confirmed.iloc[:, 4:].sum()[-1])
l2 = 'Recovered at ' + last_date + ' - ' + str(recovered.iloc[:, 4:].sum()[-1])
l3 = 'Dead at ' + last_date + ' - ' + str(deaths.iloc[:, 4:].sum()[-1])

# Это суммарные графики по 20 странам
fig, ax = plt.subplots(figsize = [16,6])
ax.plot(confirmed.iloc[:, 4:].sum(), '-', alpha = 0.6, color = 'orange', label = l1)
ax.plot(recovered.iloc[:, 4:].sum(), '-', alpha = 0.6, color = 'green', label = l2)
ax.plot(deaths.iloc[:, 4:].sum(), '-', alpha = 0.6, color = 'red', label = l3)

ax.legend(loc = 'upper left', prop=dict(size=12))
ax.xaxis.grid(which='minor')
ax.yaxis.grid()
ax.tick_params(axis = 'x', labelrotation = 90)
plt.title('COVID-19 in all countries. Top 20 countries consists {:.2%} of total confirmed infected cases.'.format(conf_tot_ratio[0]))
plt.show()


# Формируем сводную таблицу по 20 странам + Россия + Украина
confirmed_top = confirmed_top.rename(columns={str(last_date): 'total_confirmed'})
dates = [i for i in confirmed.columns[4:]]

for country in countries:

    # Находим для каждой страны общее число заразившихся, прирост их числа на текущую дату, уровень смертности
    confirmed_top.loc[country, 'total_confirmed'] = confirmed.loc[confirmed['Country/Region'] == country,:].sum()[4:][-1]
    confirmed_top.loc[country, 'last_day_conf'] = confirmed.loc[confirmed['Country/Region'] == country,:].sum()[-1] - confirmed.loc[confirmed['Country/Region'] == country,:].sum()[-2]
    confirmed_top.loc[country, 'mortality, %'] = round(deaths.loc[deaths['Country/Region'] == country,:].sum()[4:][-1]/confirmed.loc[confirmed['Country/Region'] == country,:].sum()[4:][-1]*100, 1)

    # Пиком эпидемии считаем точку максимума линии тренда.
    smoothed_conf_max = round(smooth_conf_daily[smooth_conf_daily['Country/Region'] == country].iloc[:,4:].sum().max(), 2)
    peak_date = smooth_conf_daily[smooth_conf_daily['Country/Region'] == country].iloc[:,4:].sum().idxmax()
    peak_day = dates.index(peak_date)

    # За время старта эпидемии принимаем дату, на которую колчиество заболевших превышает 1% от максимума дневных заражений
    start_day = (smooth_conf_daily[smooth_conf_daily['Country/Region'] == country].iloc[:,4:].sum() < smoothed_conf_max/100).sum()
    start_date = dates[start_day-1]

    # Записываем результаты в сводную таблицу
    confirmed_top.loc[country, 'trend_max'] = smoothed_conf_max
    confirmed_top.loc[country, 'start_date'] = start_date
    confirmed_top.loc[country, 'peak_date'] = peak_date
    confirmed_top.loc[country, 'peak_passed'] = round(smooth_conf_daily.loc[smooth_conf_daily['Country/Region'] == country, last_date].sum(), 2) != smoothed_conf_max
    confirmed_top.loc[country, 'days_to_peak'] = peak_day - start_day

    # Если пик пройдет, оцениваем  дату завершения эпидемии
    if confirmed_top.loc[country, 'peak_passed']:
          confirmed_top.loc[country, 'end_date'] = (datetime.strptime(confirmed_top.loc[country, 'peak_date']+'20', "%d.%m.%Y").date() + timedelta(confirmed_top.loc[country, 'days_to_peak'])).strftime('%d.%m.%Y')


# Отрисовываем графики по нужным странам
plot_by_country('Italy')

plot_by_country('Ukraine')

