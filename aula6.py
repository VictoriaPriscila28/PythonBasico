#tuplas, dicionarios e conjuntos

minha_lista = ['gui','joao'] # ordenado
minha_tupla = ('gui','joao') # nao é mutavel
# utilizar quando voce tiver aquele numero limitado de coisas
meu_dicionario = {'nome': 'Guilherme','idade': '27'} # tabela hash
meu_conjunto = {'Gui', 'joao'} # nao existe itens repitidos, é dinamico,nao é ordenado

print(meu_dicionario['nome'])
if 'Guilherme'in meu_dicionario.values():
    print('guilherme esta no dicionario')


for valores in meu_dicionario.values():
    print(valores)

for valores in meu_dicionario.keys():
    print(valores)

meu_dicionario['nome'] = 'joao'
print(meu_dicionario)

meu_dicionario['endereco'] = 'av. joao das neves '
meu_dicionario['telefone'] = '0123456789'
print(meu_dicionario)

meu_conjunto.add('gui')
if 'Gui' in meu_conjunto:
    print('foi encontrado dentro do conjunto')

meu_conjunto.remove('Gui')
print(meu_conjunto)
conjunto = set()
loucura = [(1,2), (2,4), (5,6), ({'joao', 'maria'}, {'gabriel'}) ]
print(loucura)
