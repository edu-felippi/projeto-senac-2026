class Converter:

    def converter_para_inteiro(self, texto: str):
        try:
            numero = int(texto)
        except ValueError:
            return 'Conversão inválida'
        
        return numero