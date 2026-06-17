def calcular_medias_alunos():
    with open('proj/arquivos/ex7/notas.txt', 'r') as arquivo:
        with open('proj/arquivos/ex7/medias_finais.txt', 'w') as final:
            for line in arquivo.readlines():
                dados = line.split(',')
                nome = dados[0]
                nota1 = float(dados[1])
                nota2 = float(dados[2])
                media = (nota1 + nota2) / 2

                final.write(f'{nome}: Media {media}\n')

if __name__ == "__main__":
    calcular_medias_alunos()