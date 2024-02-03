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

''' resolução do guilherme

EXERCICIO: Crie um software de gerenciamento bancário
Esse software poderá ser capaz de criar clientes e contas
Cada cliente possui nome, cpf, idade
Cada conta possui um cliente, saldo, limite, sacar, depositar e consultar_saldo


from cliente import Cliente
from conta import Conta

cliente1 = Cliente('Gui', '123.456.789-10', 27)


conta_do_gui = Conta(cliente1, 10.50, 1000)

print(conta_do_gui.cliente.nome, conta_do_gui.consulta_saldo())

conta_do_gui.depositar(1000.40)

print(conta_do_gui.consulta_saldo())

conta_do_gui.sacar(500)

print(conta_do_gui.consulta_saldo())

conta_do_gui.sacar(1000)

print(conta_do_gui.consulta_saldo())'''