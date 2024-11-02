class Animal:
    def __init__(self, especie):
        self.especie = especie

    def falar(self):
        return f"Este é um animal da espécie {self.especie}"

animal = Animal("Canis lupus")
print(animal.falar())
