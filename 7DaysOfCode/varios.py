rows = int(input("Enter number of rows: "))

for i in range(1, rows+1):
    # espaços à esquerda
    for space in range(rows - i):
        print(" ", end="")
    # estrelas com espaço
    for star in range(i):
        print("* ", end="")
    # quebra de linha
    print()
###########################
print("2222222222222222222")
rows = 5
for i in range(rows, 0, -1):
    print(" " * (rows-i) + "* " * i)
print("3333333333333333333")
# Lista de padrões
patterns = [
    {
        "name": "Pirâmide de estrelas",
        "description": "Imprime uma pirâmide de estrelas centralizada usando '* '",
        "code": """
rows = 5
for i in range(1, rows+1):
    print(" "*(rows-i) + "* " * i)
"""
    },
    {
        "name": "Triângulo numérico",
        "description": "Imprime números em triângulo crescente por linha",
        "code": """
rows = 5
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
"""
    },
    {
        "name": "Diamante de estrelas",
        "description": "Pirâmide completa com metade superior e inferior formando um diamante",
        "code": """
rows = 5
# metade superior
for i in range(1, rows+1):
    print(" "*(rows-i) + "* " * i)
# metade inferior
for i in range(rows-1, 0, -1):
    print(" "*(rows-i) + "* " * i)
"""
    }
]

# Iterando e mostrando cada padrão com descrição
for p in patterns:
    print(f"\n=== {p['name']} ===")
    print(f"Descrição: {p['description']}")
    print("Código:")
    print(p['code'])
    print("Saída:")
    # Executando o código de cada padrão
    exec(p['code'])
