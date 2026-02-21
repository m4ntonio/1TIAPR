nome_arquivo = input("Digite o nome do arquivo para abrir (ex: notas.txt): ")

try:
    # O 'r' significa modo de leitura (read)
    with open(nome_arquivo, 'r') as arquivo:
        read_data = arquivo.read()  # Lê o conteúdo do arquivo
        print(read_data)  # Imprime o conteúdo do arquivo
        print(f"Arquivo '{nome_arquivo}' encontrado e aberto com sucesso!")
        # Aqui você colocaria o código para ler o arquivo, se quisesse
except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado. Verifique o nome e tente novamente.")