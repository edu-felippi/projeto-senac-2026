from heroi import Heroi
from mago import Mago
from guerreiro import Guerreiro

if __name__ == "__main__":
    heroi = Heroi("Eduardo", 150)
    mago = Mago("Jorge", 80)
    guerreiro = Guerreiro("Cris", 100)

    print(heroi.atacar())
    print(mago.atacar())
    print(guerreiro.atacar())
