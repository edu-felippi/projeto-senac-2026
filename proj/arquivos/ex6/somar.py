def somar_valores_arquivo():
    soma = []
    with open('proj/arquivos/ex6/valores.txt', 'r') as arquivo:
        for line in arquivo.readlines():
            if float(line) == False:
                raise ValueError('Não foi possível converter')
            else:
                soma.append(float(line))
                linha = sum(soma)
        print(linha)
            
if __name__ == "__main__":
    somar_valores_arquivo()