#entrada e saida de arquivos
#open('arquivo.txt','w') # 2 argumentos: nome do arquivo, modo de abertura
# se voce nao colocar nenhum modo de abertura ele abre como modo 'r', modo 'read'
# modo 'w' significa escrever; o 'w' cria e pode sobreescrever
#open('arquivo.txt','r+')
#open('arquivo.txt','a') # metodo append, metodo para abrir arquivo de txt. Todo aquivo que nao for de txt é pra ser aberto com 'b'
#arquivo = open('arquivo.txt','w')

'''for i in range(0,1000):
    arquivo.write('aaaa'+  str(i)+"\n")'''
arquivo = open('arquivo.txt','r')
for linha in arquivo:
    print(linha)
