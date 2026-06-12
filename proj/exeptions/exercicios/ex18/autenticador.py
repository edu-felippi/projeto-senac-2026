from minha_excecao import ContaBloqueadaError

class Autenticador:

    senha_correta = "1234"
    tentativas = 0

    def fazer_login(self, senha_digitada: str):
        if senha_digitada != self.senha_correta:
            self.tentativas += 1
            try:
                raise ValueError('Senha Incorreta')
            except ValueError:
                print(self.tentativas)
        
        if self.tentativas > 3:
            raise ContaBloqueadaError('Sua conta foi bloqueada')