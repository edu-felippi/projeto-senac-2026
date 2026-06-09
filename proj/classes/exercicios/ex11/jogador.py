class Jogador:

    nome: str
    pontuacao: int = 0

    def __init__(self, nome: str):
        self.nome = nome
        self.pontuacao: int = 0

    def acertou_alvo(self, distancia_do_centro: float):
        if distancia_do_centro < 5:
            self.pontuacao += 100
        
        if 5 <= distancia_do_centro <= 20:
            self.pontuacao += 50

        self.pontuacao += 10