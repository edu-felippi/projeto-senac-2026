from vaga import Vaga
from veiculo import Veiculo
from excecao_veiculo import VeiculoGrandeException
from excecao_vaga import VagaOcupadaException

import datetime

class Estacionamento:
    vagas = list[Vaga | None] = [None] * 10
    vaga = Vaga()

    def __init__(self, vagas: list):
        self.vagas = vagas

    def estacionar(self, veiculo: Veiculo, numero_vaga: int, horario: datetime.time):
        if numero_vaga < 0 or numero_vaga >= len(self.vagas):
            raise IndexError("Número de vaga inválido")

        if not self.vaga.disponivel:
            raise VagaOcupadaException(f"A vaga {numero_vaga} já está ocupada")
        
        if veiculo.capacidade > self.vaga.capacidade:
            raise VeiculoGrandeException("O veículo é muito grande para esta vaga")

    def adicionar_estacionamento(self, veiculo: Veiculo, numero_vaga: int, horario: datetime.time):
        pass

    def verificar_horario(self, numero_vaga: int):
        pass

    def checkout(self, vaga: Vaga):
        pass