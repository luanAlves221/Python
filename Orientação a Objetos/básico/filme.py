class Filme:
    def __init__(self, titulo, ano, genero):
        self.titulo = titulo
        self.ano = ano
        self.genero = genero

    def info(self):
        return f"o filme {self.titulo} foi lansado no ano  {self.ano} e é do gênero {self.genero}"

filme = Filme("Fuga das galinhas", 2000, "animação")

print(filme.info())