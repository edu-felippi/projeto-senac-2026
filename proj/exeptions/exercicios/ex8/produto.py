class Produto:

    def __init__(self, nome: str, preco: float):
        if preco <= 0:
            raise ValueError('O valor não pode ser menor que 0')
        
if __name__ == "__main__":
    produto = Produto('Feijão com farinha', -12)
    print(produto)