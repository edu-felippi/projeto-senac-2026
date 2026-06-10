from empresa import Empresa


if __name__ == "__main__":
    empresa = Empresa("Empresa Legal")
    empresa.contratar("Jorge")
    assert empresa.verificar_funcionario("Jorge") == True

    empresa.demitir("Jorge")
    assert empresa.verificar_funcionario("Jorge") == False