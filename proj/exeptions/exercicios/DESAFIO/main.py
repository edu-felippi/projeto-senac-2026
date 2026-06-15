###### EXEMPLO!!! ######

class Pessoa:
    pass

if __name__ == "__main__":



    while(True):
        print("1 - Criar pessoa: ")
        print("2 - Mostrar pessoa: ")
        print("3 - Sair! ")

        escolha = int(input("\n Escolha uma opção: "))

        if escolha == 1:
            nome = input("Digite o nome da pessoa: ")
            idade = int(input(f"Digite a idade de {nome}: "))

            pessoa = Pessoa(nome, idade)

        if escolha == 2:
            print(f"O nome da pessoa é {nome} e a idade é {idade} ")

        if escolha == 3:
            break