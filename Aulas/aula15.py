#consultando clima e cotação do dolar
import requests
import json
import time
import datetime
while True:
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacao = json.loads(requisicao.text)
    print('### COTAÇÃO ###', datetime.datetime.now())
    print('Dolar:', cotacao['USDBRL']['bid'])
    print('Euro:', cotacao['EURBRL']['bid'])
    print('BTC:', cotacao['BTCBRL']['bid'])
    time.sleep(2)




