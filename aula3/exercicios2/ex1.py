def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não é permitida"

resultado_soma = adicao(10, 5)
resultado_subtracao = subtracao(10, 5)
resultado_multiplicacao = multiplicacao(10, 5)
resultado_divisao = divisao(10, 5)

# Exemplos de uso:
print("Adição:", adicao(5, 3))
print("Subtração:", subtracao(5, 3))
print("Multiplicação:", multiplicacao(5, 3))
print("Divisão:", divisao(5, 2))