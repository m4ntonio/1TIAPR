try:
    numero = int(input("Digite um número inteiro: "))
    print(f"Sucesso! Você digitou o número {numero}.")
except ValueError:
    print("Erro: Isso não é um número inteiro válido.")