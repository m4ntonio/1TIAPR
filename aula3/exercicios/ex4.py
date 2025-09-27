# Função para verificar se uma matriz é identidade
def eh_matriz_identidade(matriz):
    """
    Verifica se uma matriz é uma matriz identidade.
    Uma matriz identidade tem 1s na diagonal principal e 0s nas outras posições.
    """
    n = len(matriz)
    
    # Verifica se a matriz é quadrada
    for linha in matriz:
        if len(linha) != n:
            return False
    
    # Verifica cada elemento
    for i in range(n):
        for j in range(n):
            if i == j:  # Diagonal principal
                if matriz[i][j] != 1:
                    return False
            else:  # Fora da diagonal
                if matriz[i][j] != 0:
                    return False
    
    return True

def imprimir_matriz(matriz, nome="Matriz"):
    """Função auxiliar para imprimir matrizes de forma organizada"""
    print(f"{nome}:")
    for linha in matriz:
        print([f"{elem:3}" for elem in linha])
    print()

# Exemplo 1: Matriz identidade 3x3
print("=== EXEMPLO 1: Matriz Identidade ===")
matriz_identidade = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

imprimir_matriz(matriz_identidade, "Matriz 1")
resultado = eh_matriz_identidade(matriz_identidade)
print(f"É matriz identidade? {resultado}")
print()

# Exemplo 2: Matriz que NÃO é identidade
print("=== EXEMPLO 2: Matriz Não-Identidade ===")
matriz_nao_identidade = [
    [1, 0, 0],
    [0, 2, 0],
    [0, 0, 1]
]

imprimir_matriz(matriz_nao_identidade, "Matriz 2")
resultado = eh_matriz_identidade(matriz_nao_identidade)
print(f"É matriz identidade? {resultado}")
print()

# Exemplo 3: Matriz com zeros na diagonal
print("=== EXEMPLO 3: Matriz com Zeros na Diagonal ===")
matriz_zero_diagonal = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 0, 1]
]

imprimir_matriz(matriz_zero_diagonal, "Matriz 3")
resultado = eh_matriz_identidade(matriz_zero_diagonal)
print(f"É matriz identidade? {resultado}")
print()

# Exemplo 4: Matriz com valores decimais
print("=== EXEMPLO 4: Matriz com Decimais ===")
matriz_decimal = [
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0]
]

imprimir_matriz(matriz_decimal, "Matriz 4")
resultado = eh_matriz_identidade(matriz_decimal)
print(f"É matriz identidade? {resultado}")
print()

print("="*50)
print("=== USANDO NUMPY ===")

import numpy as np

# Criando matriz identidade com NumPy
matriz_np_identidade = np.eye(3)
print("Matriz identidade criada com np.eye(3):")
print(matriz_np_identidade)
print()

# Função para verificar identidade com NumPy
def eh_identidade_numpy(matriz):
    """Verifica se uma matriz é identidade usando NumPy"""
    matriz_np = np.array(matriz)
    identidade_esperada = np.eye(matriz_np.shape[0])
    return np.allclose(matriz_np, identidade_esperada)

# Testando diferentes matrizes
matrizes_teste = [
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]],  # Identidade
    [[1, 0, 0], [0, 2, 0], [0, 0, 1]],  # Não identidade
    [[2, 0, 0], [0, 2, 0], [0, 0, 2]],  # Múltiplo da identidade
    [[1, 1, 0], [0, 1, 0], [0, 0, 1]]   # Com elemento fora da diagonal
]

for i, matriz in enumerate(matrizes_teste, 1):
    print(f"Teste {i}:")
    imprimir_matriz(matriz)
    
    # Método manual
    resultado_manual = eh_matriz_identidade(matriz)
    
    # Método NumPy
    resultado_numpy = eh_identidade_numpy(matriz)
    
    print(f"Método manual: {resultado_manual}")
    print(f"Método NumPy: {resultado_numpy}")
    print("-" * 30)

print("\n=== INFORMAÇÕES SOBRE MATRIZ IDENTIDADE ===")
print("Uma matriz identidade I_n é uma matriz quadrada n×n onde:")
print("• Todos os elementos da diagonal principal são iguais a 1")
print("• Todos os outros elementos são iguais a 0")
print("• Propriedade: A × I = I × A = A (para qualquer matriz A compatível)")