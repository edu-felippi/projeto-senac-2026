from lampada import Lampada


if __name__ == "__main__":
    lamp = Lampada()
    assert lamp.status() != "A lâmpada está ligada"

    lamp.clicar_interruptor()
    assert lamp.status() == "A lâmpada está ligada"
    