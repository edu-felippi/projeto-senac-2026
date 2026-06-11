from divisao import Divisao

import traceback

if __name__ == "__main__":

    divisao = Divisao()

    try:
        divisao.dividir_numeros(1, 0)
    except ZeroDivisionError:
        print(traceback.format_exc())
    finally:
        b = int(input('Digite um novo número maior que zero:'))
        print(divisao.dividir_numeros(1, b))