def gravar_diario(mensagem: str):
    with open("proj/arquivos/ex1/diario.txt", "w") as arquivo:
        arquivo.write(mensagem)

if __name__ == "__main__":
    gravar_diario('Apenas um teste, hehe')