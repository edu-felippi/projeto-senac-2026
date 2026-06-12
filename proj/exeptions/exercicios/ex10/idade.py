class IdadeInvalidaError(Exception):

    def cadastrar_eleitor(self, idade: int):
        self.idade = idade
        if idade < 16:
            raise IdadeInvalidaError('Idade insuficiente')
        
if __name__ == "__main__":
    idade = IdadeInvalidaError()
    print(idade.cadastrar_eleitor(15))