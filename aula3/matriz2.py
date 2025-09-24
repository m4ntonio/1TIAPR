# Matrix inicial
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Adicionando um elemento (100) na segunda linha na primeira posição
matriz[1].insert(1, 100)

# Imprimindo a matriz atualizada
for linha in matriz:
    print(linha)