from CarrinhoCompras import CarrinhoDeCompras


if __name__ == "__main__":
    carrinho = CarrinhoDeCompras()
    carrinho.adicionar_item("chocolate", 30.0)
    carrinho.adicionar_item("celular", 120.0)
    assert carrinho.calcular_total() == 150.0