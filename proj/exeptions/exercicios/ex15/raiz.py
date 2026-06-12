from minha_excecao import NumeroNegativoError

def calcular_raiz_quadrada(numero: float):
    if numero < 0.0:
        raise NumeroNegativoError('Coloque apenas números positivos')
    
    if not isinstance(numero, float):
        raise TypeError('Coloque apenas números')