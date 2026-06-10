from carro import Carro


if __name__ == "__main__":
    carro = Carro("Peugeot", 2026)
    assert carro.viajar(-10) == "Distância não válida."

    carro.viajar(10)
    assert carro.odometro == 10

    carro.viajar(5)
    assert carro.odometro == 15