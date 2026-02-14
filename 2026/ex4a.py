class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print("Depósito realizado")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Saque realizado")
        else:
            print("Saldo insuficiente")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular} | Saldo: R$ {self.saldo}")


class ContaCorrente(Conta):
    def __init__(self, titular, saldo=0, limite=0):
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            print("Saque realizado (com limite)")
        else:
            print("Limite insuficiente")


class ContaPoupanca(Conta):
    def __init__(self, titular, saldo=0, juros=0.01):
        super().__init__(titular, saldo)
        self.juros = juros

    def render_juros(self):
        self.saldo += self.saldo * self.juros
        print("Juros aplicados")


# ===== TESTE (ESSA PARTE FAZ APARECER RESULTADO) =====

cc = ContaCorrente("Mario", 1000, 500)
cp = ContaPoupanca("Ana", 2000, 0.05)

cc.mostrar_saldo()
cc.sacar(1300)
cc.mostrar_saldo()

print("-----")

cp.mostrar_saldo()
cp.render_juros()
cp.mostrar_saldo()
