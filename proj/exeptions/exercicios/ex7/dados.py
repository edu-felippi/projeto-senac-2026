def processar_dados(lista: list, indice: int):

    if indice >= len(lista):
        raise IndexError('Índice não existe')
    
    if not isinstance(lista[indice], int):
        raise TypeError('Tipo não suportado para operação matemática')
        
    return lista[indice] / 2

if __name__ == "__main__":

    try:
        processar_dados([2, 'a', 5, 3, 4], 1)
    except IndexError as e:
        print(e)
    except TypeError as e:
        print(e)
