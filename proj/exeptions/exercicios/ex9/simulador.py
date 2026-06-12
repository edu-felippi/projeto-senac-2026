def simular_banco_de_dados(comando: str):
    pass

if __name__ == "__main__":
    try:
        print(simular_banco_de_dados(34))
    except Exception as e:
        print(e)
    finally:
        print(simular_banco_de_dados('DELETE'))