#nome = 'victoria'
#tipo = type(nome)
'''idade = 22
altura = 1.58
tipo_nome = type(nome)
tipo_idade = type(idade)'''

"""tipo_nome = type(nome)
tipo_idade = type(idade)
tipo_altura = type(altura)
print(tipo_nome)
print(idade)
print(tipo_idade)
print(altura)
print(tipo_altura)"""
#concatenação
'''print(nome, 'tem', idade, 'anos e', altura, 'de altura')
print(tipo_nome)
print(tipo_idade)

nome2 = input('Digite seu nome: ')
print(nome2, 'tem', idade, 'anos e', altura, 'de altura')'''

''' Exercicio
Faça um formulario que pergunte: nome, cpf, endereço, idade, altura e telefone.
E imprima isso em um relatorio organizado.'''

print('---------------------------------------------------------------')
print("Para prosseguir digite seus dados: ")
nome = input('Digite seu nome: ')
idade = input('digite sua idade: ')
cpf = input('Digite seu cpf: ')
altura = float(input('digite sua altura: '))
telefone = input('Digite seu numero de telefone: ')
endereco = input('Digite seu endereço: ')

print('Leia com atenção se suas informações estão corretas: ')
print('Seu nome é',nome,',voce tem', idade,'anos e', altura, 'metros de altura. \n' 
'Seu CPF é:', cpf,'.', 'Seu telefone de contato é: ', telefone, ',e por fim, seu endereço é:', endereco, '.')

res = str(input('Esta tudo certo?')).upper().strip()

if res == 'sim':
    print('entao tudo certo')
else:
    print('por favor refaça seu cadastro')