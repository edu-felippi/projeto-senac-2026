def analisar_dimensoes_casa(nome_arquivo: str):
    try:
        with open(nome_arquivo, 'r') as planta:
            perimetro = 0
            area = 0
            for line in planta.readlines():
                perimetro += line.count('=')
                area += line.count(' ')
            print(f'O perímetro das paredes é {perimetro}')
            print(f'A área útil construída é {area}')
    except ValueError:
        print('A planta está vazia')
    
if __name__ == "__main__":
    analisar_dimensoes_casa(
        'proj/arquivos/ex11/planta_casa.txt')