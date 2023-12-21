# Atividade de Checkout da Disciplina de Algoritmos e Programação I/Ciências de Dados/UFMS

# Função para cadastrar uma nova fruta ou legume em um mercado:
quantidade = int(input("Quantos produtos você deseja cadastrar? "))
list = []

n = 1
while n <= quantidade:
    n = n + 1
    nome = input("Digite o nome da fruta ou legume que deseja cadastrar: ")
    preco = float(input("Digite o preço deste produto: "))
    list = list + [(nome, preco)]
    print(f"Produto {nome} cadastrado com sucesso!")

continuar_cadastro = input("Deseja continuar cadastro? ")
if continuar_cadastro == ("Sim" or "sim"):
    nome = input("Digite o nome da fruta ou legume que deseja cadastrar: ")
    preco = float(input("Digite o preço deste produto: "))
    list = list + [(nome, preco)]
    print(f"Produto {nome} cadastrado com sucesso!")
    print(list)

else:
    print(list)
