from veiculo import Veiculo
from carro import Carro

caminhao_rosa = Veiculo('rosa',6,'ford', 10)
print(caminhao_rosa)
print(type(caminhao_rosa))
print('caminhao rosa')
print('Cor:',caminhao_rosa.cor,
      'Marca:', caminhao_rosa.marca,
      'Tanque1:',caminhao_rosa.tanque)
caminhao_rosa.abastecer(20)
print('Tanque', caminhao_rosa.tanque)
caminhao_rosa.abastecer(80)
print('Tanque', caminhao_rosa.tanque)

print("")

print("Carro Azul")
carro_azul = Veiculo('azul',4,'bwm',30)
print('Cor:',carro_azul.cor)
print('Marca:', carro_azul.marca)
print('Tanque1:',carro_azul.tanque)
carro_azul.abastecer(10)
print('Tanque2',carro_azul.tanque)
carro_azul.abastecer(70)
print('Tanque3',carro_azul.tanque)

#carro_azul.abastecer(35)
#print("tanque:", carro_azul.tanque) # aumentou para 65l

