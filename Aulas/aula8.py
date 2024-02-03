#Argumentos de linha de comando
import sys

argumentos = sys.argv #arg1 metod // arg2 - n1 // arg3 -n2
#print(argumentos)

def soma(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

if argumentos[1] == 'soma':
    resp = soma(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == 'sub':
    resp = sub(float(argumentos[2]), float(argumentos[3]))

print(resp)

#linha de comando python3 aula8.py soma 1234 627 = 1861.0
#linha de comando python3 aula8.py soma 300  223.1 = 76.9

