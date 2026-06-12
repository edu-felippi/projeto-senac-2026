from minha_excecao import AnatomiaError
from guitarra import Guitarra
from instrumento import Instrumento

if __name__ == "__main__":
    instrumento = Instrumento()
    guitarra = Guitarra()

    try:
        print(instrumento.tocar())
    except AnatomiaError as e:
        print(e)
    finally:
        print(guitarra.tocar())