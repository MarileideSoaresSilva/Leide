# Definição das variáveis e entrada dos valores da distância percorrida e do consumo médio do veículo:
distanciaPercorrida = float(input("Qual a distância percorrida pelo veículo em Km? "))
consumoMedio = float(input("Qual o consumo médio do veículo em Km/Litro? "))

# Cálculo da quantidade de combustível gasta pelo veículo:
combustivelGasto = (distanciaPercorrida / consumoMedio)
print(float("%.2f" % combustivelGasto), "Litros")