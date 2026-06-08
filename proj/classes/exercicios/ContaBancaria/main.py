from conta_bancaria import ContaBancaria


if __name__ == "__main__":
    conta = ContaBancaria("Eduardo")
    conta.depositar(25)
    print(conta)
