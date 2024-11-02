class Carro:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def info(self):
        return f"Esse carro é da marca {self.marca} e do ano {self.ano}"

meu_carro = Carro("Ford", 2022)
print(meu_carro.info())
