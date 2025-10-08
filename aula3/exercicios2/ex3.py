def media_lista(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

numeros = [10, 20, 40, 50]
media = media_lista(numeros)
print(f"A média é: {media}")