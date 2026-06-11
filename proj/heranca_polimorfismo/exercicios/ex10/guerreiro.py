from heroi import Heroi

class Guerreiro(Heroi):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.forca_fisica = 40

    def atacar(self):
        self.forca_fisica *= 2
        return self.forca_fisica