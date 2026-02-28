caminho_arquivo = 'dados.bin'

with open(caminho_arquivo, mode='rb') as arquivo_binario:
    numeros_lidos = []
    while True:
        bytes_lidos = arquivo_binario.read(4)
        if not bytes_lidos:
            break
        numero = int.from_bytes(bytes_lidos, byteorder='little')
        numeros_lidos.append(numero)

print(f'Os números lidos do arquivo {caminho_arquivo} são: {numeros_lidos}')

with open('numeros_lidos.txt', mode='w') as arquivo_texto:
    for numero in numeros_lidos:
        arquivo_texto.write(f'{numero} ')
        
