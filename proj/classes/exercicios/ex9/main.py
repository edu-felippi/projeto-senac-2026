from BichinhoVirtual import BichinhoVirtual


if __name__ == "__main__":
    bichinho = BichinhoVirtual("Jorge")
    bichinho.alimentar()
    assert bichinho.fome == 35

    bichinho.brincar()
    assert bichinho.felicidade == 75