class Veiculo:
    def __init__(self, cor, rodas, marca,tanque):# o objeto passa ele mesmo dentro // metodo init é o construtor
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque

    def abastecer(self,litros):
        self.tanque += litros


