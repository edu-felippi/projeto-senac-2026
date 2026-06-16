def filtrar_erros():

    filtro = []
    with open('proj/arquivos/ex5/sistema.log', 'r') as arquivo, open('proj/arquivos/ex5/alertas_criticos.txt', 'a') as alerta:
        for line in arquivo.readlines():
            if 'ERROR' in line.startswith():
                alerta.write(line)
                


if __name__ == "__main__":
    filtrar_erros()