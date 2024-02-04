#Bibliotecas, PIP e Requisições Web
#gerenciador de pacotes: pip
# beautiful soup bs4
import requests

'''requisicao = requests.get('https://solyd.com.br')
print(type(requisicao))
print(requisicao.status_code)
print(requisicao.text) # mostra o codigo fonte'''
cabecalho = {'User-agent': 'Brave Browser',
             'Referer': 'https://solyd.com.br'}
meus_cookies = {'ultima visita': '10-10-2020'}
dados = {'username': 'victoria',
         'password': 'victoria123'}
texto = None
try:
    requisicao = requests.get('https://putsreq.com/7Hb5zjwKSpBstg3fThaG',
                              headers= cabecalho,
                              cookies = meus_cookies,
                              data=dados)
    texto = requisicao.text
except Exception as e:
    print('requisição deu erro',e)
print(texto)
