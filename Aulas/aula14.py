# expressoẽs regulares
''' mini liguagem que te ajuda a identificar padroes'''
import re
string_de_teste = 'o gatos é bonito'
padrao = re.search(r'gat\w\w',string_de_teste) # raw string
print(padrao.group())
#print(r'oi pessoal\n segunda linha')

if padrao:
    print(padrao.group())
else:
    print('padrao nao encontrado')
