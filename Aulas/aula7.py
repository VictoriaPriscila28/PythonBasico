# Funções e metodos
def soma(numero1,numero2):
    resp = numero1 + numero2
    return resp

retorno = soma(75,1289)
print(retorno)

def tem_sete_itens(argumento):
    if len(argumento)== 7:
        return True
    else:
        return False

print(tem_sete_itens(('oi pessoal')))
if tem_sete_itens(('1234567')):
    print('realmente tem sete letras')

'''
exercício

Escreva uma função que receba um objeto de coleção(lista,tupla, conjunto)
e retorna o valor do maior numero dentro dessa coleção.
Faça outra função que retorne o menor numero dessa coleção'''

datas_anv = [28, 11, 6, 5, 8, 26]
def maximo_elemento():
    return max(datas_anv)
print(maximo_elemento())

def minimo_elemento():
    return min(datas_anv)
print(minimo_elemento())

#resulução do guilherme
def maior(colecao):
    maior_item = colecao[0]
    for item in colecao:
        if item > maior_item:
            maior_item = item
    return maior_item
print(maior([1,2,3,4,5,6,7,8,76,1265,0,27]))

def menor(colecao):
    menor_item = colecao[0]
    for item in colecao:
        if item < menor_item:
            menor_item = item
    return menor_item

print(menor([1,-2, 1.2,87.2,1289,-7,0]))




