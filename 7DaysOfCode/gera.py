# -*- coding: utf-8 -*-
import io, sys

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
        "name": "Triângulo invertido numérico",
        "description": "Triângulo decrescente de números",
        "code": """
rows = 5
for i in range(rows, 0, -1):
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
for i in range(1, rows+1):
    print(" "*(rows-i) + "* " * i)
for i in range(rows-1, 0, -1):
    print(" "*(rows-i) + "* " * i)
"""
    },
    {
        "name": "Quadrado de números",
        "description": "Imprime um quadrado de números com linhas e colunas iguais",
        "code": """
rows = 5
for i in range(1, rows+1):
    for j in range(1, rows+1):
        print(j, end=" ")
    print()
"""
    },
    {
        "name": "Diagonal de números",
        "description": "Imprime números apenas na diagonal, espaços nos outros lugares",
        "code": """
rows = 5
for i in range(1, rows+1):
    for j in range(1, rows+1):
        if i == j:
            print(i, end=" ")
        else:
            print(" ", end=" ")
    print()
"""
    },
    {
        "name": "Pirâmide invertida",
        "description": "Pirâmide de estrelas invertida",
        "code": """
rows = 5
for i in range(rows, 0, -1):
    print(" "*(rows-i) + "* " * i)
"""
    },
    {
        "name": "Triângulo de letras",
        "description": "Imprime um triângulo crescente com letras do alfabeto",
        "code": """
rows = 5
import string
letters = string.ascii_uppercase
for i in range(1, rows+1):
    print(" ".join(letters[:i]))
"""
    },
    {
        "name": "Pirâmide de números com espaço",
        "description": "Pirâmide de números centralizada",
        "code": """
rows = 5
for i in range(1, rows+1):
    print(" "*(rows-i) + " ".join(str(j) for j in range(1, i+1)))
"""
    },
    {
        "name": "Quadrado de asteriscos",
        "description": "Quadrado sólido de '*'",
        "code": """
rows = 5
for i in range(rows):
    print("* " * rows)
"""
    }
]

filename = "manual_padroes_python.md"

with open(filename, "w", encoding="utf-8") as f:
    f.write("# Manual de Padrões Python\n\n")
    for p in patterns:
        f.write(f"## {p['name']}\n")
        f.write(f"**Descrição:** {p['description']}\n\n")
        f.write("**Código:**\n```python\n")
        f.write(p['code'].strip() + "\n```\n")
        f.write("**Saída:**\n```\n")
        # Captura a saída do código
        old_stdout = sys.stdout
        sys.stdout = mystdout = io.StringIO()
        exec(p['code'])
        sys.stdout = old_stdout
        f.write(mystdout.getvalue() + "\n```\n\n")

print(f"Manual gerado com sucesso: {filename}")
