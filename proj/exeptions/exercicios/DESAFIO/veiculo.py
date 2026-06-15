from onibus import Onibus
from carro import Carro
from van import Van

class Veiculo:
    
    def __init__(self, placa: str, peso: float, cor: str, condutor: str, capacidade: int):
        self.placa = placa
        self.peso = peso
        self.cor = cor
        self.condutor = condutor
        self.capacidade = capacidade