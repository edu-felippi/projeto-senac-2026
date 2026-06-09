class Lampada:

    def __init__(self):
        self.ligada = False

    def clicar_interruptor(self):
        if self.ligada == False:
            self.ligada = True
        else:
            self.ligada = False
        
    def status(self):
        if self.ligada == False:
            return f"A lâmpada está desligada"
        else:
            return f"A lâmpada está ligada"