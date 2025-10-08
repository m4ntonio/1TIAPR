def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    return sum(1 for letra in texto if letra in vogais)

frase = input("Digite uma frase: ")
print(f"Número de vogais: {contar_vogais(frase)}")