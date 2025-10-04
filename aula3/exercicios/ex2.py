# Criação da matriz 2x2
matriz = [
    [1, 2],
    [3, 4]
]

# Definição do escalar
escalar = 3

# Multiplicação da matriz pelo escalar
resultado = []
for i in range(2):
    linha = []
    for j in range(2):
        linha.append(matriz[i][j] * escalar)
    resultado.append(linha)

# Exibe o resultado
print("Matriz multiplicada pelo escalar:")
for linha in resultado:
    print(linha)