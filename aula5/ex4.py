arquivo = "arq1.txt"

try:
    with open(arquivo, 'r') as file:
        linhas = file.readlines()
        num_linhas = len(linhas)  # Correção: usando len() para contar as linhas
        
        print(f'O arquivo tem {num_linhas} linhas.')
        print(f'Conteúdo do arquivo (lista de linhas):')
        print(linhas)

except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")