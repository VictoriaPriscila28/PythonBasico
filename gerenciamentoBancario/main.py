from conta import Conta
from cliente import Cliente


cliente1 = Cliente('victoria','123456789101','22')
conta1 = Conta('victoria',1000,2000)

print("Informações do cliente")
print('Nome:',cliente1.nome)
print('CPF:',cliente1.cpf)
print('Idade:',cliente1.idade)

print("")

print("Informações da conta do cliente")
print('Saldo:',conta1.saldo)
print('Limite:',conta1.limite)

print("")
print("Depositos e saques")
conta1.depositar(500)
print('novo valor',conta1.saldo)
conta1.sacar(100)
print('novo valor apos saque',conta1.saldo)
conta1.sacar(2000)
print('novo valor apos 2° saque',conta1.saldo)
