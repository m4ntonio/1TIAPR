try:
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))
except ValueError:
    print("Erro: Pelo menos uma das entradas não é um número inteiro válido.")
else:
    # Se a conversão deu certo lá no 'try', nós somamos aqui no 'else'
    soma = num1 + num2
    print(f"A soma dos números é: {soma}")