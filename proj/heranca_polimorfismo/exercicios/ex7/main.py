from flauta import Flauta
from violao import Violao
from bateria import Bateria


if __name__ == "__main__":
    flauta = Flauta()
    violao = Violao()
    bateria = Bateria()
    instrumentos = [violao, flauta, bateria]

    for instrumento in instrumentos:
        print(instrumento.tocar())