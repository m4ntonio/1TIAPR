class Pessoa:
    def __init__(self, nome, idade, peso, altura, sexo):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo

    def descrever(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso}, Altura: {self.altura}, Sexo: {self.sexo}"

p1 = Pessoa("Carlos", 40, 80, 1.75, "Masculino")
print(p1.descrever())
