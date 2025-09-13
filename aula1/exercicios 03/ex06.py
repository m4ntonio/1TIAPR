try:
    idade = int(input("Digite sua idade: "))
    if idade <= 0:
        print("Idade inválida. Por favor, digite um valor positivo.")
    elif idade >= 16:
        print("Você pode votar.")
    else:
        print("Você não pode votar.")
except ValueError:
    print("Por favor, digite um número inteiro válido para a idade.")