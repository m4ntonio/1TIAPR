arquivo = open('ex1.txt', 'r')
texto = arquivo.read()
palavras = len(texto.split())
arquivo.close()

print(f'O arquivo tem {palavras} palavras.')