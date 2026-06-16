def registrar_pontuacao(nome_jogador: str, pontos: int):
    with open('proj/arquivos/ex3/ranking.txt', 'a') as arquivo:
        arquivo.write(f'Nome: {nome_jogador} - Pontos: {pontos}\n')

if __name__ == "__main__":
    registrar_pontuacao('Jorge', 98)