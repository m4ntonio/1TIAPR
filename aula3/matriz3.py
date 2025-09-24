# Matrix inicial
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Usando del para remover a segunda linha
del matriz[1]

# Imprimindo a matriz após a remoção da segunda linha
print("Matriz após remover a segunda linha:")
for linha in matriz:
    print(linha)

# Usando pop para obter o elemento da terceira coluna da primeira linha
elemento = matriz[0].pop(2)
print("\nElemento removido:", elemento)

# Imprimindo a matriz após a remoção do elemento
print("\nMatriz após remoção do elemento:")
for linha in matriz:
    print(linha)



