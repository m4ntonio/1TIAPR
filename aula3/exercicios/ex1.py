# Criação das matrizes
matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Soma das matrizes
soma = []
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(matriz1[i][j] + matriz2[i][j])
    soma.append(linha)

# Exibe o resultado
print("Matriz Soma:")
for linha in soma:
    print(linha)