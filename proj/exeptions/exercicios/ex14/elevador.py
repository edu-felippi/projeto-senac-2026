from minha_excecao import ElevadorSobrecargadoError

class Elevador:

    def entrar_pessoa(self, peso_pessoa: float):
        self.peso_pessoa = peso_pessoa
        peso_total = 0
        if peso_total + peso_pessoa > 400:
            raise ElevadorSobrecargadoError('Sobrecarga no elevador')
