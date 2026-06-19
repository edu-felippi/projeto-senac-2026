def inventariar_moveis(nome_arquivo: str):
    inventario = {}

    with open(nome_arquivo, 'r') as arquivo:
        for index_linha, linha in enumerate(arquivo.readlines()):
            for index_coluna, caracter in enumerate(linha):
                if caracter.isupper():
                    inventario[caracter] = (index_linha, index_coluna)
                    
    return inventario

if __name__ == "__main__":
    print(inventariar_moveis(
        'proj/arquivos/ex11/planta_casa.txt'))