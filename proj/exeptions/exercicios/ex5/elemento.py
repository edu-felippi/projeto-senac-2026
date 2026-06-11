def obter_elemento(lista: list, indice: int):
    if indice >= len(lista):
        raise IndexError('Posição inexistente')
    
    return lista[indice]
        
if __name__ == "__main__":
    print(obter_elemento([5, 6, 2, 2, 1], 1))