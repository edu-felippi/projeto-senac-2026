def limpar_arquivo(origem, destino):
    with open(origem, 'r') as arquivo, open(destino, 'w') as final:
            for line in arquivo.readlines():
                 linha_limpa = line.strip()
                 if linha_limpa:
                      final.write(linha_limpa + '\n')

if __name__ == "__main__":
    limpar_arquivo('proj/arquivos/ex9/dados_sujos.txt', 'proj/arquivos/ex9/dados_limpos.txt')