from conta import Conta

class ContaEstudante(Conta):

    def render_bonus(self):
        self.saldo += 10