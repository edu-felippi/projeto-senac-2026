from carro import Carro


if __name__ == "__main__":
    carro = Carro("Peugeot", 2026)

    carro.viajar(25)
    assert carro.odometro == 25

    carro.viajar(-10)
    assert 'Distância não válida'