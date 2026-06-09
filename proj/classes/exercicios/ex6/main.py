from termometro import Termometro


if __name__ == "__main__":
    termometro = Termometro(20)
    
    termometro.diminuir(25)
    assert termometro.alerta_clima() == 'Congelando'

    termometro.aumentar(27)
    assert termometro.alerta_clima() == 'Agradável'

    termometro.aumentar(8)
    assert termometro.alerta_clima() == 'Muito Quente'
    