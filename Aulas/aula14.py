# expressoẽs regulares
''' mini liguagem que te ajuda a identificar padroes'''
import re
import requests
#string_de_teste = 'jffnjfk@fnkdf.com'
#padrao = re.search(r'gat\w+',string_de_teste) # raw string
requisicao = requests.get('https://datametricapesquisas.com.br/fale-conosco/')
padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+',requisicao.text)
#print(padrao.group())
#print(r'oi pessoal\n segunda linha')
#https://regex101.com/
if padrao:
    print(padrao)
else:
    print('padrao nao encontrado')
