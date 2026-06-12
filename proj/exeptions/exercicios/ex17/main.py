from usuario import Usuario
from admin import Admin
from comum import Comum

def deletar_banco_de_dados(usuario_objeto):
    if not isinstance(usuario_objeto, Admin):
        raise PermissionError('Você deve ser um Admin para deletar este objeto')
    
if __name__ == "__main__":
    comum = Comum()
    admin = Admin()

    deletar_banco_de_dados(comum)