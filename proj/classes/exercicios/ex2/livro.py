class Livro:

    titulo: str
    autor: str
    quantidade_copias: int

    def __init__(self, titulo: str, autor: str, quantidade_copias: int):
        self.titulo = titulo
        self.autor = autor
        self.quantidade_copias = quantidade_copias

    def vender(self):
        self.quantidade_copias -= 1
    
    def reabastecer(self, quantidade: int):
        self.quantidade_copias += quantidade