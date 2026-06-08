class Aluno:

    nome: str
    notas: list

    def __init__(self, nome: str, notas: list):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    
    def verificar_situacao(self):
        if self.calcular_media >= 7.0:
            return f"Aprovado"
        elif self.calcular_media 