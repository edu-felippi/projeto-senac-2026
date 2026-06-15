class Vaga:

    def __init__(self, capacidade: int):
        self.veiculo = None
        self.capacidade = capacidade
        self.horario_entrada = None
        self.disponivel = True