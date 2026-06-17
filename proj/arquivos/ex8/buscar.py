def buscar_palavra_no_texto(palavra_alvo: str):
    with open('proj/arquivos/ex8/documento.txt', 'r') as arquivo:
        for indice, line in enumerate(arquivo.readlines(), start=1):
            if palavra_alvo in line:
                print(f'Linha {indice}: {line}')

if __name__ == "__main__":
    buscar_palavra_no_texto('erros')