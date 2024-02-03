
class Conta:
    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self._saldo = saldo
        self.limite = limite

    @property
    def saldo(self):
        return self._saldo

    def verificar_saldo(self):
        print('Saldo atual:', self.saldo)

    def ajustar_limite(self, valor):
        self.limite += valor
        if self.limite > self.saldo:
            print('Limite excede o saldo')
        else:
            print('Limite aceito')

    def sacar(self, valor):
        if self.saldo - valor < -self.limite:
            print('Saque excede o limite')
        else:
            self._saldo -= valor
            print('Saque de', valor, 'realizado com sucesso')

    def depositar(self, valor):
        self._saldo += valor
        print('Depósito de', valor, 'realizado com sucesso')







