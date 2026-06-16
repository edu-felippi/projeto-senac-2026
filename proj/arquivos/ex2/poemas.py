def ler_poema():
    try:
        with open('proj/arquivos/ex2/poema.txt', 'r') as arquivo:
            poema = arquivo.read()
            print(poema)
    except FileNotFoundError:
        print('Arquivo não encontrado')

if __name__ == "__main__":
    ler_poema()