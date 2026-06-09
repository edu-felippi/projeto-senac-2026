from aluno import Aluno


if __name__ == "__main__":
    aluno = Aluno("Eduardo", [3,4,5,2])
    resultado = aluno.verificar_situacao()
    assert resultado == 'Reprovado'

    aluno2 = Aluno("Eduardo", [10,8,9,9])
    resultado2 = aluno2.verificar_situacao()
    assert resultado2 == 'Aprovado'

    aluno3 = Aluno("Eduardo", [7,6,5,6])
    resultado3 = aluno3.verificar_situacao()
    assert resultado3 == 'Recuperação'