#abrir um arquivo para leitura e escrita
with open("ex1.txt", "r+") as file:
    conteudo = file.read()
    file.write("\nAdicionando mais conteudo.")