class BichinhoVirtual:

    nome: str
    fome: int = 50
    felicidade: int = 50

    def __init__(self, nome:str):
        self.nome = nome

    def alimentar(self):
        if self.fome - 15 < 0:
            self.fome = 0
        else:
            self.fome = self.fome - 15
            self.felicidade = self.felicidade + 5

    def brincar(self):
        if self.felicidade + 20 > 100:
            self.felicidade = 100
        else:
            self.felicidade = self.felicidade + 20
            self.fome = self.fome + 10