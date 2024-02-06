''' Resolução do exercicio 13 feito pelo Guilherme, entretanto o código não executa corretamente por conta da url fornecida.
A api ao longo dos anos sofreu alterações e foi-se necessario possuir uma apikey para utilizar os serviços. Contudo,
diferente do exemplo feito na aula 13 e inserido apenas a apikey, nesse em questão foi necessario mudar um pouco.
A grande diferença foi na concatenação de strings na url. Abaixo terá o codigo corrigo e a resolução do Guilherme a nivel de comparação.'''
import requests
import json

def lista_filmes(titulo):
    lista = []
    try:
        for i in range(1, 11):
            print('Pesquisando na página:', i)
            req = requests.get(f'http://www.omdbapi.com/?apikey=846cc761&type=movie&s={titulo}&page={i}') #alteração
            resposta = json.loads(req.text)
            if resposta['Response'] == 'True':
                for filme in resposta['Search']:
                    tit = filme['Title']
                    ano = filme['Year']
                    string = f'{tit} ({ano})'
                    lista.append(string)
            else:
                print('Fim das páginas')
                break
    except Exception as e: # alteração para que aceite qualquer tipo de erro
        print('Erro de conexão:', e)
    return lista

sair = False
while not sair:
    op = input('Pesquise por um filme ou digite SAIR: ')
    if op.upper() == "SAIR":
        sair = True
    else:
        lista_de_filmes = lista_filmes(op)
        print('Filmes encontrados:', len(lista_de_filmes))
        for filme in lista_de_filmes:
            print(filme)


'''
RESOLUÇÃO GUILHERME 

import requests
import json

def lista_filmes(titulo):
    lista = []
    for i in range(1, 101):
        try:
            print('Pesquisando em pagina:', i)
            url = 'http://www.omdbapi.com/?s=' + titulo + '&type=movie&page=' + str(i)
            req = requests.get(url)
            resposta = json.loads(req.text)
            if resposta['Response'] == 'True':
                for filme in resposta['Search']:
                    tit = filme['Title']
                    ano = filme['Year']
                    string = tit + ' (' + ano + ')'
                    lista.append(string)
            else:
                print('Fim das paginas')
                break
        except:
            print('Conexao falhou')
    return lista

sair = False
while not sair:
    op = input('Pesquise por um filme ou digite SAIR: ')
    if op == "SAIR":
        sair = True
    else:
        lista_de_filmes = lista_filmes(op)
        print('Filmes encontrados:', len(lista_de_filmes))
        for filme in lista_de_filmes:
            print(filme)'''

