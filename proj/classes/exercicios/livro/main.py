from livro import Livro


if __name__ == "__main__":
    livro = Livro("Dom Casmurro", "Machado de Assis", 4)
    livro.reabastecer(3)
    print(livro.quantidade_copias)