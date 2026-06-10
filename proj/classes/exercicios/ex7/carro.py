class Carro:

    modelo: str
    ano: int
    odometro: float = 0

    def __init__(self, modelo: str, ano: int):
        self.modelo = modelo
        self.ano = ano

    def viajar(self, distancia: float):
        if distancia < 0:
            return "Distância não válida."
        
        self.odometro += distancia