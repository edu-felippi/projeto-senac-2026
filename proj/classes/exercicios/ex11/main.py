from jogador import Jogador


if __name__ == "__main__":
    jogador = Jogador("Eduardo")
    jogador.acertou_alvo(3)
    jogador.acertou_alvo(15)
    assert jogador.pontuacao == 150