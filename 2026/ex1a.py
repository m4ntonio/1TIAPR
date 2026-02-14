class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def info(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def info(self):
        return f"{super().info()}, Raça: {self.raca}"

class Gato(Animal):
    def __init__(self, nome, idade, cor):
        super().__init__(nome, idade)
        self.cor = cor

    def info(self):
        return f"{super().info()}, Cor: {self.cor}"

class Passaro(Animal):
    def __init__(self, nome, idade, pode_voar):
        super().__init__(nome, idade)
        self.pode_voar = pode_voar

    def info(self):
        return f"{super().info()}, Pode voar: {'Sim' if self.pode_voar else 'Não'}"

# Exemplos de instanciamento
c = Cachorro("Rex", 5, "Labrador")
print(c.info())

g = Gato("Mia", 3, "Preto")
print(g.info())

p = Passaro("Piu", 2, True)
print(p.info())

