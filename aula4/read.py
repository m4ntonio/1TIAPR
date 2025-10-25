#abre um arquivo no modo de leitura
with open('arquivo.txt', 'r') as file:
    conteudo = file.read()
    print(conteudo)

#abre o arquivo no modo de eitura
with open('arquivo.txt', 'r') as file:
    linha1 = file.readline()
    linha2 = file.readline()
    linha3 = file.readline()
    print(linha1)
    print(linha2)
    print(linha3)