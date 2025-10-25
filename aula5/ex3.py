palavra = input('Digite uma palavra a ser buscada: ')

with open('ex1.txt', 'r') as arquivo:
    
    linha = arquivo.readline()
    numero_linha = 1
    while linha:
        if palavra in linha:
            print(f'Palavra encontrada na linha {numero_linha}: {linha.strip()}')
        linha = arquivo.readline()
        numero_linha += 1

    if not palavra in linha:
        print('Palavra não encontrada no arquivo.')