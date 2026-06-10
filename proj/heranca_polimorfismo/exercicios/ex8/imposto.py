from calculador import CalculadorDeImposto

class ImpostoArtigoLuxo(CalculadorDeImposto):

    def calcular(self, valor):
        return valor * 0.20