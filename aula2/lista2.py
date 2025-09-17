#1
numeros = [1, 2, 3, 4, 5]
soma = sum(numeros)
print("A soma dos números é:", soma)

resultado = 0
for numero in numeros:
    resultado += numero
print("A soma dos números é:", resultado)


#2
string = ["Python", "linguagem", "programação"]
print(", ".join(string))


#3
numeros = [2, 4, 6, 8, 73]
maior = max(numeros)
print("O maior número é:", maior)


#4
nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]
nome = "Mario"

if nome in nomes:
    print(f"{nome} está presente na lista.")
else:
    print(f"{nome} não está presente na lista.")


#5
numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)

print("A média dos números é:", average)