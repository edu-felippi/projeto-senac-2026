from veiculo import Veiculo
from datetime import datetime

class Vaga:

    def __init__(self, capacidade: int):
        self.veiculo = None
        self.capacidade = capacidade
        self.horario_entrada = datetime = None
        self.disponivel = True

    def alocar_carro(self, veiculo: Veiculo, horario: datetime.time):
        self.veiculo = veiculo
        self.disponivel = False
        self.horario_entrada = horario

    def liberar_vaga(self):
        pass