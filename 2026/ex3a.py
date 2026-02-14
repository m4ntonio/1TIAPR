class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        return f"Nome: {self.nome} | Idade: {self.idade}"


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, curso, nota):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.curso = curso
        self.nota = nota


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, salario, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.salario = salario
        self.setor = setor


# Teste
a = Aluno("João", 20, "A123", "TI", 8.5)
f = Funcionario("Maria", 35, "Gerente", 5000, "Financeiro")

print(a.mostrar_dados())
print(f.mostrar_dados())
