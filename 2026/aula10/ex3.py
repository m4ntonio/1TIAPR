linguagens = ["Python", "C++", "Java", "Ruby"]

try:
    indice = int(input("Digite um número de 0 a 3 para ver um item da lista: "))
    elemento = linguagens[indice]
    print(f"Sucesso! No índice {indice}, o elemento é: {elemento}")

except IndexError:
    print("Erro: Índice fora do limite! Você digitou um número que não existe na lista.")
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite apenas números inteiros.")
