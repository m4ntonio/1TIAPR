class Pessoa:
    def __init__(self, nome, idade, peso, altura, sexo):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo

    def descrever(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso}, Altura: {self.altura}, Sexo: {self.sexo}"

    def envelhecer(self, anos=1):
        self.idade += anos

# Exemplo de uso
p1 = Pessoa("Pedro", 20, 65, 1.75, "Masculino")  # Troque pelos seus dados
p1.envelhecer(3)  # Agora a idade será 21
print(p1.descrever())
