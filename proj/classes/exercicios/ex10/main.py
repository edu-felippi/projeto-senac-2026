from CarrinhoCompras import CarrinhoDeCompras


if __name__ == "__main__":
    carrinho = CarrinhoDeCompras()
    carrinho.adicionar_item("chocolate", 30)
    carrinho.adicionar_item("celular", 120)

    print(carrinho.calcular_total())