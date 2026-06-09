from livro import Livro


if __name__ == "__main__":
    livro = Livro("Dom Casmurro", "Machado de Assis", 4)
    livro.vender()
    assert livro.quantidade_copias == 3
    livro.reabastecer(3)
    assert livro.quantidade_copias == 6
    