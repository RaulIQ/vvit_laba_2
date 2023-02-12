import requests


city = 'Moscow, RU'
appid = '8b4e8bf3c2932d3cdbd8834c9dcd43b7'

# Прогноз погоды на сегодня 
# r = requests.get('http://api.openweathermap.org/data/2.5/weather', params = {'q':'city' ,'units':'metric', 'lang':'ru', 'APPID':appid})
# data = r.json()

# print("Город:", city)
# print('Погодные условия:', data['weather'][0]['description'])
# print("Температура:", data['main']['temp'])
# print("Минимальная температура:", data['main']['temp_min'])
# print("Максимальная температура", data['main']['temp_max'])

# Прогноз погоды на неделю
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <", i['weather'][0]['description'], ">")
    print("____________________________")