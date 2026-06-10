from veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, marca: str, ano: int):
        super().__init__(marca, ano)