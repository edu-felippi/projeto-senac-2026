from conta_estudante import ContaEstudante


if __name__ == "__main__":

    conta_estudante = ContaEstudante()
    conta_estudante.render_bonus()
    print(conta_estudante.saldo == 110)