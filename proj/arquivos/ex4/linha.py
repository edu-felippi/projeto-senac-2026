def contar_linhas_arquivos(nome_arquivo: str):
    with open(nome_arquivo) as arquivo:
        count = 0
        for line in arquivo.readlines():
            if line.endswith('\n') or line.startswith('\n'):
                count += 1