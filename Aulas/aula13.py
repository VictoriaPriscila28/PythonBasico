#API, JSON e consultando listas de filmes
'''import requests
import json
req = None

api_key = '5ecb3c17'
try:
    req = requests.get('http://www.omdbapi.com/?t=interstellar{5ecb3c17}')
except:
    print('erro na conexao')
    exit()

dicionario = json.loads(req.text)
print(dicionario)'''

import json
import requests


def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?apikey=846cc761&t=' + titulo)

        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro na conexão')
        return None


def printar_detalhes(filme):
    print('Titulo:', filme['Title'])
    print('Ano:', filme['Year'])
    print('Diretor:', filme['Director'])
    print('Atores:', filme['Actors'])
    print('Nota:', filme['imdbRating'])
    print('')

sair = False
while not sair:
    op = input('Escreva o nome de um filme ou SAIR para fechar: ')
    if op == 'SAIR':
        sair = True
    else:
        filme = requisicao(op)
    if filme['Response'] == 'False':
        print('Filme não encontrado')
    else:
        printar_detalhes(filme)