'''Estruturas de laço while e for'''

'''nomes =['guilherme','marcelo','joao','julia']
print(nomes)
for nome in nomes:
    print(nome)'''

'''lista_de_numeros = range(5)
for i in lista_de_numeros:
    print(i)'''


'''lista_de_numeros2 = range(0,100,2) # do 0 ao 100, passando de 2 em 2; imprimiu so os pares
for item in lista_de_numeros2:
    print(item)


for i in range(len(nomes)):
    print(nomes[i])
    nomes.append('oii')
print(nomes)'''

'''palavra = 'guilherme junqueira'
for letra in palavra:
    print(letra)'''

i = 0
'''while i < 10:
    print('i ainda é menor do que 10:', i)
    i = i + 1
print('acabou  o while', i)'''

'''i = i + 10
i += 1
print(i)'''

'''lista_frutas = ['apple', 'banana', 'cherry', 'strawberry']
contador = 0

for fruta in lista_frutas:
    contador += 1

print(contador)
print(len(lista_frutas))

numero = 0
while True:
    print(numero)
    if numero == 20:
        numero += 1
        break
    numero += 1

print('saiu do while')'''

'''Exercicio 
Faça um programa que leia a quantidade de pessoas que serao convidadas para uma festa.
Apos isso o programa ira perguntar o nome de todas as pessoas 
e colocar numa lista de convidados. Apos isso ira imprimir todos os nomes da lista
'''

lista_convidados = ['joao', 'maria', 'jose', 'claudia','raquel','jaqueline', 'afonso', 'clemente']

print('Ao todo serão convidados',len(lista_convidados), 'pessoas')

for convidado in lista_convidados:
    if convidado in lista_convidados:
        print('qual seu nome?')
        print('meu nome é', convidado)

else:
    print('acabou a lista de convidados')

print('Esses sao os nomes de todas as pessoas da lista: ', lista_convidados)