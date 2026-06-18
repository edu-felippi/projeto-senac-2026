def fazer_backup_dados(nome_arquivo_original):
    try:
        with open(nome_arquivo_original, 'r') as arquivo, open('proj/arquivos/ex10/dados.csv.bak', 'w') as final:
            line = arquivo.read()
            final.write(line)
            print('Backup realizado com sucesso')
    except FileNotFoundError:
        print('Arquivo não encontrado')
    except Exception as e:
        print(f'Ocorreu um erro imprevisto: {e}')

if __name__ == "__main__":
    fazer_backup_dados('proj/arquivos/ex10/dados_originais.csv')