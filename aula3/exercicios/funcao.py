def saudar(nome):
    print(f"Olá, {nome}!")

saudar("João")

def saudar2(nome):
    return f"Olá, {nome}!"

print(saudar2("Maria"))

def soma(a, b):
    return a + b

resultado = soma(5, 3)
print(f"A soma é: {resultado}")

def soma2(a, b, c):
    return a + b + c

resultado2 = soma2(1, 2, 9)
print(f"A soma é: {resultado2}")