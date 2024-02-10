import requests
import json
apikey = '0dc7be46024c0edd446e536760d8cfeb'

cidade= input('Digite o nome da cidade: ')
requisicao = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={cidade}&appid={apikey}')
print(json.loads(requisicao.text))
resp = json.loads(requisicao.text)
resp_dict = resp[0]
lat = resp_dict['lat']
lon = resp_dict['lon']
print(lat)
print(lon)

requisicao2 = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}')
print(json.loads(requisicao2.text))

tempo = json.loads(requisicao2.text)
print('tempo:',tempo['weather'][0]['main'])
print('temperatura:',float(round(tempo['main']['temp']- 273.15)))