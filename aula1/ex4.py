# 1. Área de um círculo com raio 5
raio = 5
pi = 3.14159
area = pi * (raio ** 2)
print("1. Área do círculo:", area)

# 2. Conversão de Fahrenheit para Celsius
fahrenheit = 100
celsius = (fahrenheit - 32) * 5/9
print("2. Temperatura em Celsius:", celsius)

# 3. Total gasto com livros e canetas
preco_livro = 25
quantidade_livros = 3
preco_caneta = 5
quantidade_canetas = 2

total = (preco_livro * quantidade_livros) + (preco_caneta * quantidade_canetas)
print("3. Total gasto: R$", total)

# 4. Tempo gasto em uma viagem
distancia = 150  # km
velocidade_media = 60  # km/h

tempo = distancia / velocidade_media
print("4. Tempo da viagem:", tempo, "horas")

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"A Temperatura em Celsius é: {celsius:.2f}")