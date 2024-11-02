class Celular:
    def __init__(self, marca, modelo, bateria=50):
        self.marca = marca
        self.modelo = modelo
        self.bateria = bateria

    def usar_bateria(self):
        if self.bateria >= 10:
            self.bateria -= 10
        else:
            print("A bateria está baixa!")

celular = Celular("Samsung", "Galaxy S20")
celular.usar_bateria()
celular.usar_bateria()
celular.usar_bateria()


print(celular.bateria)
