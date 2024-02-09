#consultando clima e cotação do dolar
import requests
import json
requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacao = json.loads(requisicao.text)
print(cotacao)

# Fazendo a requisição para obter os dados do dólar americano
requisicao2 = requests.get('https://economia.awesomeapi.com.br/last/USD')
print('### COTAÇÃO ###')
# Carregando os dados da resposta JSON
cotacao2 = json.loads(requisicao.text)
# Imprimindo os dados da cotação do dólar americano
print('Dolar:', cotacao2)

'''
{'USDBRL': {'code': 'USD', 'codein': 'BRL', 'name': 'Dólar Americano/Real Brasileiro', 
'high': '4.9925', 'low': '4.9598', 'varBid': '-0.0177', 'pctChange': '-0.35', 'bid': '4.9738', 
'ask': '4.9748', 'timestamp': '1707489685', 'create_date': '2024-02-09 11:41:25'},
 'EURBRL': {'code': 'EUR', 'codein': 'BRL', 'name': 'Euro/Real Brasileiro', 'high': '5.3838',
  'low': '5.3486', 'varBid': '-0.016', 'pctChange': '-0.3', 'bid': '5.3614', 'ask': '5.3694', 
  'timestamp': '1707489681', 'create_date': '2024-02-09 11:41:21'},
'BTCBRL': {'code': 'BTC', 'codein': 'BRL', 'name': 'Bitcoin/Real Brasileiro', 'high': '238500', 
'low': '225000', 'varBid': '10405', 'pctChange': '4.62', 'bid': '235818', 'ask': '235869', 
'timestamp': '1707489642', 'create_date': '2024-02-09 11:40:42'}}'''