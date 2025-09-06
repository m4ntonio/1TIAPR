nome = input("Digite seu nome: ")
print("Olá, " + nome + "!")

num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")

resultado = num1 + num2
print("A concatenação dos números é: " + resultado)

idade = int(input("Digite sua idade: "))

#if idade >= 18:
#    print("Você é maior de idade.")
#else:
#    print("Você é menor de idade.")
if idade > 17 and idade < 66:
    print("Você é um adulto.")
elif idade > 65:
    print("Você é um idoso.")
else:
    print("Você é uma criança ou adolecente.")