def buscar_letra_na_lista(lista_de_strings: list, indice_lista: int, indice_palavra: int):
    try:
        palavra = lista_de_strings[indice_lista]
        letra = palavra[indice_palavra]
        print(f"Letra encontrada: {letra}")

    except IndexError as erro:
        print(f"Erro: {str(erro)}")

if __name__ == "__main__":
    print(buscar_letra_na_lista(['carro', 'ônibus', 'caminhão'], 1, 7))