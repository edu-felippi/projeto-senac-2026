from dispositivo import Dispositivo

class Celular(Dispositivo):
    
    def __init__(self, nome: str, bateria: int):
        self.bateria = bateria
        super().__init__(nome)