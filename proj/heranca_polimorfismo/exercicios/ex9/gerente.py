from funcionario import Funcionario

class Gerente(Funcionario):

    def trabalhar(self):
        return super().trabalhar() + ' e revisando relatórios da equipe.'