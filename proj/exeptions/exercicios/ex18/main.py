from minha_excecao import ContaBloqueadaError
from autenticador import Autenticador

if __name__ == "__main__":
    autenticador = Autenticador()
    autenticador.fazer_login('2356')
    autenticador.fazer_login('2376')
    autenticador.fazer_login('5463')
    autenticador.fazer_login('4562')