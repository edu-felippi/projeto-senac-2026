def gerar_planta_de_csv(nome_arquivo_csv: str, nome_arquivo_txt: str):

    matriz = [[' ' for _ in range(10)] for _ in range(10)]

    with open(nome_arquivo_csv, 'r') as arquivo:
        next(arquivo)

        for line in arquivo.readlines():
            tipo, linha, coluna = line.split(',')
            l = int(linha)
            c = int(coluna)

            if tipo == 'Parede':
                matriz[l][c] = '='
            elif tipo == 'Mesa':
                matriz[l][c] = 'M'

    with open(nome_arquivo_txt, 'w') as final:
        for line_matriz in matriz:
            line_final = ' '.join(line_matriz)
            final.write(line_final + '\n')

if __name__ == "__main__":
    gerar_planta_de_csv(
        'proj/arquivos/ex13/coordenadas_planta.csv', \
            'proj/arquivos/ex13/planta.txt')