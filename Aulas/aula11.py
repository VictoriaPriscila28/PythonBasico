# Tratamentos de erros e exceções (TRY e EXCEPT)

# prever que podem acontecer possiveis erros com o usuario
import time
try:
    a = 1200 / 0
except ZeroDivisionError:
    print('Divisao por zero nao dá pra fazer')

try:
    aevvfdggdr()
except NameError:
    print('Voce digitou alguma coisa errada')

try:
    aevvfdggdr()
except Exception as erro: # 'erro' entra como uma variavel que vai armazenar o erro propriamente dito
    print('Aconteceu algum erro:', erro)

#sempre que for fazer uma aplicação que possivelmente vai dar erro, utilizar try e except

def abre_arquivo():
    try:
        arquivo = open('arquivodoido.txt')
        return True
    except Exception as erro:
        print('Aconteceu algum erro:', erro)
        return False

while not abre_arquivo():
    print('Tentando abrir o arquivo')
    time.sleep(5)
print('consegui abrir o arquivo')

