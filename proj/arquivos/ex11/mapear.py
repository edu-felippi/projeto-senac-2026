def mapear_paredes_planta(nome_arquivo: str):
    try:
        coordenadas = []
        with open(nome_arquivo, 'r') as planta:
            for index_linha, linha in enumerate(planta.readlines()):
                for index_coluna, caracter in enumerate(linha):
                    if caracter == '=':
                        coordenadas.append((index_linha, index_coluna))
        return coordenadas
    except FileNotFoundError:
        return 'Arquivo não encontrado'
    
if __name__ == "__main__":
    coordenadas = mapear_paredes_planta(
        'proj/arquivos/ex11/planta_casa.txt')
    print(coordenadas)