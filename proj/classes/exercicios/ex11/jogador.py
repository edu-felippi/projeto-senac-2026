class Jogador:

    nome: str

    def __init__(self, nome: str):
        self.nome = nome
        self.pontuacao: int = 0

    def acertou_alvo(self, distancia_do_centro: float):
        if distancia_do_centro < 5.0:
            self.pontuacao += 100
        elif 5.0 <= distancia_do_centro <= 20.0:
            self.pontuacao += 50
        else:
            self.pontuacao += 10