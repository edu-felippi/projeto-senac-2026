def limpar_arquivo(origem, destino):
    with open(origem, 'r') as arquivo:
        for line in arquivo.readlines():
            linha_limpa -= line.strip('\n')
    with open(destino, 'w') as final:
        final.write()

if __name__ == "__main__":
    limpar_arquivo('proj/arquivos/ex9/dados_sujos.txt', 'proj/arquivos/ex9/dados_limpos.txt')