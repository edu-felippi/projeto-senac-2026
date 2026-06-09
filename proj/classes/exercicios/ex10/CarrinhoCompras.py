class CarrinhoDeCompras:

    

    def __init__(self):
        self.itens = []
        self.precos = []

    def adicionar_item(self, nome_produto: str, preco_produto: float):
        self.itens.append(nome_produto)
        self.precos.append(preco_produto)

    def calcular_total(self):
        return sum(self.precos)