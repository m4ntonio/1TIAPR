numero = int(input("Digite um número par: "))

while numero % 2 != 0:
    print("Número inválido. Tente novamente.")
    numero = int(input("Digite um número par: "))
print(f"Obrigado! {numero} é um número par!")