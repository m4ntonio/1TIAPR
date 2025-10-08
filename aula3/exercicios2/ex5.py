def fatorial(n):
    if n < 0:
        return None
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

numero = int(input("Digite um número: "))
print(f"O fatorial de {numero} é {fatorial(numero)}")