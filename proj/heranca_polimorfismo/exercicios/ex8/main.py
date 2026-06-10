from calculador import CalculadorDeImposto
from imposto import ImpostoArtigoLuxo


if __name__ == "__main__":
    calculador = CalculadorDeImposto()
    imposto = ImpostoArtigoLuxo()

    print(calculador.calcular(100))
    print(imposto.calcular(100))