def filtrar_erros():
    with open('proj/arquivos/ex5/sistema.log', 'r') as arquivo:
        with open('proj/arquivos/ex5/alertas_criticos.txt', 'w') as alerta:
            for line in arquivo.readlines():
                if line.startswith('ERROR'):
                    alerta.write(line)
                


if __name__ == "__main__":
    filtrar_erros()