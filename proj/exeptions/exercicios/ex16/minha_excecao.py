class SaldoInsuficienteError(Exception):
    
    def __init__(self, *args, saldo_faltante: any):
        super().__init__(*args)
        self.saldo_faltante = saldo_faltante
        