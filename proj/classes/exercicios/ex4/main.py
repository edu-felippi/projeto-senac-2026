from conta_bancaria import ContaBancaria


if __name__ == "__main__":
    conta = ContaBancaria("Eduardo")
    saque = conta.sacar(2)
    assert saque is False

    conta.depositar(25.0)
    assert conta.saldo == 25.0
