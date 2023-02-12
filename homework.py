import requests


city = 'Moscow, RU'
appid = '8b4e8bf3c2932d3cdbd8834c9dcd43b7'

# Прогноз погоды на сегодня 
# r = requests.get('http://api.openweathermap.org/data/2.5/weather', params = {'q':'city' ,'units':'metric', 'lang':'ru', 'APPID':appid})
# data = r.json()

# print('скорость ветра:', data['wind']['speed'])
# print('Видимость', data['visibility'])

# Прогноз погоды на неделю
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
	print('Скорость ветра:', i['wind']['speed'])
	print('Видимость:', i['visibility'])
	print('_______________________________')