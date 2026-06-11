class Divisao:

    def dividir_numeros(self, a: int, b: int):
        if b == 0:
            raise ZeroDivisionError('Erro: Não é possível dividir por zero.')
        return a / b