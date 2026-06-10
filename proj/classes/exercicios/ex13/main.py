from agenda import Agenda


if __name__ == "__main__":
    agenda = Agenda()
    agenda.salvar_contato("Jorge", 51991234567)
    print(agenda.buscar_telefone("Jorge"))