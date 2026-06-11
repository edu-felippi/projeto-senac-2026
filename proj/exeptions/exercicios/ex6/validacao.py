def validar_usuario(nome: str):
    if len(nome) < 3:
        raise ValueError('Insira pelo menos 3 caracteres')
    
    return 'Usuário válido'

if __name__ == "__main__":
    print(validar_usuario(''))