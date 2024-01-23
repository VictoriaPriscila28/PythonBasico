#strings e listas
frase = 'Oi, tudo bem'
lista_nomes = ['joao', 'maria', 'jose', 'claudia', 'joao']
lista_nomes.append('lorena') # insere na ultima
lista_nomes.remove('joao')
lista_nomes.insert(1, 'creosvaldo')
lista_nomes[0] = 'robervania'
contador_joao = lista_nomes.count('joao')
print(len(lista_nomes))
print(contador_joao)
print(lista_nomes)
print(lista_nomes[0])
print(frase[0:10])
print(frase[::-1])
print(frase.lower())
frase_nova = frase + ' como vai voce?'
print(frase_nova)
#lista_nomes.clear()
