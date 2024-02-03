#operadores logicos
#tabela verdade
'''a = 50
b = 20
if a > b and 'abacaxi' == 'uva':
    print(a, 'é maior que', b)
else:
    print(a, 'nao é maior que', b)

print(not True)
print(not False)
idade = 50
if not idade == 50:
    print('voce nao tem 50 anos')
else:
    print('voce tem 50 anos')'''

''' Exercicio
Faça um programa que pergunte a idade, a altura e o pesp de uma pessoa, calcule
e decida  se ela esta apta a entrar no exercito.
Para entrar no exercito é preciso ter mais de 18 anos. 
Pesar mais ou igual a 60 kilos e medir mais de 1,70m
'''
peso = float(input('digite seu peso: '))
idade = int(input('digite sua idade: '))
altura = float(input('digite sua altura:  '))

if peso >= 60 and idade > 18 and altura >= 1.70:
    print('voce esta apto a entrar no exercito')
else:
    print('voce nao vai entrar no exercito')

