nome_arquivo = input("Digite o nome do arquivo para abrir (ex: texto.txt): ")

try:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        # Lê todas as linhas do arquivo e as guarda em uma lista
        linhas = arquivo.readlines()
except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado. Verifique o nome digitado.")
else:
    # Se o arquivo abriu normalmente, contamos o tamanho da lista de linhas
    total_linhas = len(linhas)
    print(f"Sucesso! O arquivo tem {total_linhas} linha(s).")