from minha_excecao import SaldoInsuficienteError

class ContaBancaria:

    def sacar(self, valor: float):
        self.valor = valor
        self.saldo = 100.0
        if self.saldo < self.valor:
            raise SaldoInsuficienteError("O saldo é insuficiente", saldo_faltante = self.valor - self.saldo)
        return self.saldo
    
if __name__ == "__main__":
    try:
        conta = ContaBancaria()
        conta.sacar(150)
    except SaldoInsuficienteError as e:
        print(f"Erro: {e}")
        print(f"Valor que causou o erro: {e.saldo_faltante}")