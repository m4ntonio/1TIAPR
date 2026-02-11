class veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def display_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}"

class Carro(veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Portas: {self.portas}"

v = veiculo("Toyota", "Corolla", 2020)
print(v.display_info())

c = Carro("Ford", "Fiesta", 2018, 4)
print(c.display_info())