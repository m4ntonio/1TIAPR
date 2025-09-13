# 1. Verifica se um número é positivo, negativo ou zero
num = float(input("Digite um número: "))
if num > 0:
    print("O número é positivo.")
elif num < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")


# 2. Verifica se um número é par ou ímpar
num = int(input("Digite um número: "))
if num % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")


# 3. Verifica se um ano é bissexto
ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")


# 4. Verifica se um caractere é vogal ou consoantesssssssss
caractere = input("Digite uma letra: ").lower()
if caractere in "aeiou":
    print("É uma vogal.")
elif caractere.isalpha():
    print("É uma consoante.")
else:
    print("Não é uma letra.")


# 5. Calcula preço com desconto se quantidade > 10
preco_unitario = float(input("Digite o preço unitário do produto: "))
quantidade = int(input("Digite a quantidade comprada: "))
total = preco_unitario * quantidade

if quantidade > 10:
    total *= 0.9  # aplica 10% de desconto

print(f"O valor total da compra é: R$ {total:.2f}")


# 6. Verifica se pode votar (idade mínima 16)
idade = int(input("Digite sua idade: "))
if idade >= 16:
    print("Você pode votar.")
else:
    print("Você não pode votar.")
