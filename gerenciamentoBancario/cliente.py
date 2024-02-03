

class Cliente:
    def __init__(self, nome,cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

'''essa foi a alteração que o Guilherme fez, no caso ao colocar str
o retorno já vem com as indicações corretas, sem a necessidade de adicionar
isso no main.Nesse caso quando for utilizar isso no main apenas colocaria print(cliente1)
     def __str__(self):
        return "Nome: " + self.nome + "\nCPF: " + self.cpf + "\nIdade: " + str(self.idade)
        '''
