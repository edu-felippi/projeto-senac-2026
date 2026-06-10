class Agenda:

    def __init__(self):
        self.nomes = []
        self.telefones = []

    def salvar_contato(self, nome: str, telefone: int):
        self.nomes.append(nome)
        self.telefones.append(telefone)

    def buscar_telefone(self, nome_pesquisado: str):
        if nome_pesquisado in self.nomes:
            self.telefones = self.nomes[nome_pesquisado]
            return self.telefones
        else:
            return "Contato não encontrado"