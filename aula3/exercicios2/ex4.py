def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for char in texto:
        if char in vogais:
            contador += 1
    return contador

frase = input("Digite uma frase: ")
print(f"Número de vogais: {contar_vogais(frase)}")