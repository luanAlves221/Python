class Computador:
    def __init__(self, marca, memoriaRam, armazenamento):
        self.marca = marca
        self.memoriaRam = memoriaRam
        self.armazenamento = armazenamento

    def detalhes(self):
        return f"esse computador é da marca {self.marca} com {self.memoriaRam} GB de ram e {self.armazenamento} de armazenamento (SSD)"

computador = Computador("Dell", 16, 512)
print(computador.detalhes())

