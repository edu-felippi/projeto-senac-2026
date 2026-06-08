from lampada import Lampada


if __name__ == "__main__":
    lamp = Lampada()
    lamp.clicar_interruptor()
    print(lamp.status())