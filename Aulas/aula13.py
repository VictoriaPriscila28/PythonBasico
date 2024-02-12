#API, JSON e consultando listas de filmes

import json
import requests


def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?apikey=&t=' + titulo + '&type=movie')

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
    print('Prêmios', filme['Awards'])
    print('Poster:', filme['Poster'])
    print('')

sair = False
while not sair:
    op = input('Escreva o nome de um filme ou SAIR para fechar: ')
    if op == 'SAIR':
        sair = True
        print('Saindo...')
    else:
        filme = requisicao(op)
        if filme['Response'] == 'False':
            print('Filme não encontrado')
        else:
            printar_detalhes(filme)


'''Exercicio
Fazer um programa que faça uma pesquisa com o parametro s'''
