class Carro:

    modelo: str
    ano: int
    odometro: float = 0

    def __init__(self, modelo: str, ano: int):
        self.modelo = modelo
        self.ano = ano
        self.odometro = 0

    def viajar(self, distancia: float):
        if distancia > 0:
            self.odometro = self.odometro + distancia
            return self.odometro
        return "Distância não válida"