class Sinal:

    def verificar_sinal(numero: int):
        if numero < 0:
            raise ValueError('O número não pode ser negativo')
        
    if __name__ == "__main__":

        verificar_sinal(-1)