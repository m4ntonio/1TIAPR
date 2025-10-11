def numero_primo(n):
    if n < 2:
        return False
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True

numero = int(input("Digite um número: "))
if numero_primo(numero):
    print(f"{numero} é primo.")
else:
    print(f"{numero} não primo.")
