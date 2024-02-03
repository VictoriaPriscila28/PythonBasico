from veiculo import Veiculo
'''herdou, nao precisou copiar todo o codigo anterior'''

class Carro(Veiculo):
    def __init__(self,cor, marca,tanque):
        Veiculo.__init__(self,cor,4,marca,tanque)

    def abastecer(self,litros):
        if self.tanque + litros > 50:
            print('Erro: tanque com incapacidade inferior')
        else:
            self.tanque += litros
