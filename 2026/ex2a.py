# Classe base
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def mostrar_info(self):
        return f"Produto: {self.nome} | Preço: R$ {self.preco}"


# Classe filha 1
class Eletronico(Produto):
    def __init__(self, nome, preco, garantia, marca):
        super().__init__(nome, preco)
        self.garantia = garantia
        self.marca = marca

    def detalhes_eletronico(self):
        return f"Marca: {self.marca} | Garantia: {self.garantia} meses"


# Classe filha 2
class Alimento(Produto):
    def __init__(self, nome, preco, validade, peso):
        super().__init__(nome, preco)
        self.validade = validade
        self.peso = peso

    def detalhes_alimento(self):
        return f"Validade: {self.validade} | Peso: {self.peso} kg"


# Testando
e = Eletronico("Notebook", 3500, 12, "Dell")
a = Alimento("Arroz", 25, "10/12/2026", 5)

print(e.mostrar_info())
print(e.detalhes_eletronico())

print(a.mostrar_info())
print(a.detalhes_alimento())
