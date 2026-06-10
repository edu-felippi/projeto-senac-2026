class Empresa:

    nome_empresa: str

    def __init__(self, nome_empresa: str):
        self.nome_empresa = nome_empresa
        self.funcionarios = []

    def contratar(self, nome_funcionario: str):
        self.funcionarios.append(nome_funcionario)

    def demitir(self, nome_funcionario: str):
        self.funcionarios.remove(nome_funcionario)

    def verificar_funcionario(self, nome_funcionario: str):
        if nome_funcionario in self.funcionarios:
            return True
        else:
            return False