from espada import Espada
from pedra import PedraComum
from pocao import Pocao
from inutil import ItemInutilException
from full_slot import InventarioCheioException

class Inventario:
    pedra_comum = PedraComum()
    espada = Espada()
    pocao = Pocao()
    inventario = []

    def guardar_item(self, objeto_item):
        if objeto_item == self.pedra_comum:
            raise ItemInutilException()
        
        if len(self.inventario) > 3:
            raise InventarioCheioException()