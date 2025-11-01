class Pessoa:
    def __init__(self, nome, idade, peso, altura, sexo):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo

    def descrever(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso}, Altura: {self.altura}, Sexo: {self.sexo}"

    def envelhecer(self):
        self.idade += 1

    def comparar_idade(self, outra_pessoa):
        if self.idade > outra_pessoa.idade:
            return f"{self.nome} é mais velho(a) que {outra_pessoa.nome}."
        elif self.idade < outra_pessoa.idade:
            return f"{self.nome} é mais novo(a) que {outra_pessoa.nome}."
        else:
            return f"{self.nome} e {outra_pessoa.nome} têm a mesma idade."

# Exemplo de uso
p1 = Pessoa("Carlos", 30, 75, 1.80, "Masculino")
p2 = Pessoa("Ana", 30, 65, 1.65, "Feminino")
print(p1.comparar_idade(p2))
