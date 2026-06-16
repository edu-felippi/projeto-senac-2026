from vaga import Vaga
from veiculo import Veiculo
from onibus import Onibus
from van import Van
from carro import Carro
from excecao_veiculo import VeiculoGrandeException
from excecao_vaga import VagaOcupadaException
from datetime import datetime

class Estacionamento:
    vagas = list[Vaga | None] = [None] * 10
    vaga = Vaga()

    def __init__(self, vagas: list):
        self.vagas = vagas

    def estacionar(self, veiculo: Veiculo) -> int:
        pass

    def adicionar_estacionamento(self, veiculo: Veiculo, numero_vaga: int, horario: datetime.time):
        pass

    def verificar_horario(self, numero_vaga: int) -> float:
        if numero_vaga < 0 or numero_vaga >= len(self.vagas):
            raise IndexError("Número de vaga inválido")
        
        if self.vaga.disponivel or self.vaga.horario_entrada is None:
            return 0.0
        
        agora = datetime.now()
        diferenca = agora - self.vaga.horario_entrada
        return diferenca.total_seconds() / 60

    def checkout(self, vaga: Vaga):
        pass