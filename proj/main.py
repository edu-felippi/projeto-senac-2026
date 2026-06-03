############# Exercícios: Aula 1 #############

def calcular_area_triangulo(base: float, altura: float):
    area = (base * altura) / 2
    print(f"A área do triângulo é: {area}")

def temperatura_fahrenreit(tc: float):
    temperatura = (tc * (9/5)) + 32
    print(f"A temperatura em fahrenreit é: {temperatura}")

def converte_em_dolares(reais: float):
    dolares = reais / 5.04
    print(f"O valor em dólares é: {dolares}")

############# Exercícios: Aula 2 #############

def salario_apos_desconto(salario: float):
    salario_resultante = salario * 0.85
    return salario_resultante

def verificar_membro(nome: str, idade: int):
    if nome == "Eduardo" and idade >= 16:
        return "Bem vindo!"
    return "Vaza daqui!"
    
def eh_par(numero: int):
    if numero % 2 == 0:
        return True
    else:
        return False

def classificar_pop(idade: int) -> str:
    if idade < 12:
        return "Criança"
    elif idade >= 12 and idade <= 17:
        return "Adolescente"
    else:
        return "Adulto"

def calcular_bonus(salario: float, anos_empresa: int):
    if anos_empresa > 5:
        return salario * 0.1
    else:
        return salario * 0.05
    
def encontrar_maior(a: float, b: float, c: float):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
def tipo_triangulo(lado1: float, lado2: float, lado3: float):
    if (lado1 + lado2) > lado3 \
        or (lado3 + lado2) > lado1 \
            or (lado1 + lado3) > lado2:
        
        if lado1 == lado2 == lado3:
            return "Equilátero"
        elif (lado1 != lado2 != lado3):
            return "Escaleno"
        else:
            return "Isóceles"
    
def aprovar_saque(saldo: float, valor_saque: float):
    if valor_saque <= saldo and valor_saque % 10 == 0:
        return True
    else:
        return False
    
############# Exercícios: Aula 3 #############

frutas = ['maçã', 'banana', 'laranja', 'morango']

def primeira_fruta(frutas: list):
    return frutas[0]


animais = ['gato', 'cachorro', 'passarinho', 'coelho']

def ultimo_animal(animais: list):
    return animais[-1]

# Exercício 3
compras = []

def adicionar_compras(compras: list):
    compras.append('arroz')
    compras.append('feijão')
    compras.append('batata')
    return compras

# Exercício 4
notas = [7.5, 8.0, 6.0, 9.5, 10.0]

def quantidade_notas(notas: list):
    return len(notas)

# Exercício 5
cores = ['vermelho', 'verde', 'azul']

def mudar_cor(cores: list):
    cores[1] = 'amarelo'
    return cores

# Exercício 6
tarefas = ['estudar', 'limpar quarto', 'lavar louça']

def esvaziar_tarefas(tarefas: list):
    tarefas.clear()
    return tarefas

# Exercício 7
respostas = ['Sim', 'Não', 'Sim', 'Sim', 'Não', 'Sim']

def contar_sim(respostas: list):
    return respostas.count('Sim')

# Exercício 8
fila = ['Ana', 'Bruno', 'Carlos', 'Diego']

def remover_ultimo(fila: list):
    return fila.pop()

# Exercício 9
canais = ['Globo', 'SBT', 'Record', 'Band']

def posicao_sbt(canais: list):
    return canais.index('SBT')

# Exercício 10
dias = ['Segunda', 'Quarta', 'Quinta']

def ajustar_terca(dias: list):
    dias.insert(1, 'Terça')
    return dias

# Exercício 11
numeros = [10, 20, 30, 40, 50, 60]

def tres_primeiros(numeros: list):
    return numeros[0:3]

# Exercício 12
convidados = ['Alice', 'Bob', 'Arthur', 'Carol']

def remover_arthur(convidados: list):
    convidados.remove('Arthur')
    return convidados

# Exercício 13
letras = ['A', 'B', 'C', 'D', 'E']

def inverter_lista(letras: list):
    letras.reverse()
    return letras

# Exercício 14
pontos = [45, 12, 89, 5, 23]

def ordenar_pontos(pontos: list):
    pontos.sort()
    return pontos

# Exercício 15
valores = [12, 5, 8, 22, 9, 15]

def soma_extremos(valores: list):
    return valores[0] + valores[5]

# Exercício 16
ingredientes = ['ovo', 'farinha', 'açúcar', 'leite']

def tem_chocolate(ingredientes: list):
    if 'chocolate' in ingredientes:
        return True
    else:
        return False

# Exercício 17    
amigos_escola = ['Pedro', 'Lucas']
amigos_bairro = ['Mariana', 'Julia']

def juntar_amigos(amigos_escola: list, amigos_bairro: list):
    amigos_escola.extend(amigos_bairro)
    return amigos_escola

# Exercício 18
anos = [2018, 2019, 2020, 2021, 2022, 2023, 2024]

def ultimos_tres(anos: list):
    return anos[-3: ]

# Exercício 19
brinquedos = ['carrinho', 'boneca', 'bola', 'pião']

def remover_brinquedo_seguro(brinquedos: list, item: str):
    if item in brinquedos:
        brinquedos.remove(item)
        return brinquedos
    else:
        return 'Este brinquedo não está na lista!'
    
# Exercício 20
lista = [2, 4, 5, 3, 7, 8]

def trocar_extremos(lista: list):
    lista[0], lista[-1] = lista[-1], lista[0]
    return lista

############# Rodar código: Aula 3 #############
if __name__ == '__main__':
    print("resultado exercício 1:")
    fruta = primeira_fruta(frutas)
    print(fruta)

    print("\n resultado exercício 2:")
    animal = ultimo_animal(animais)
    print(animal)

    print("\n resultado exercício 3:")
    compra = adicionar_compras(compras)
    print(compra)

    print("\n resultado exercício 4:")
    nota = quantidade_notas(notas)
    print(nota)

    print("\n resultado exercício 5:")
    cor = mudar_cor(cores)
    print(cor)

    print("\n resultado exercício 6:")
    tarefa = esvaziar_tarefas(tarefas)
    print(tarefa)

    print("\n resultado exercício 7:")
    resposta = contar_sim(respostas)
    print(resposta)

    print("\n resultado exercício 8:")
    removido = remover_ultimo(fila)
    print(removido)

    print("\n resultado exercício 9:")
    sbt = posicao_sbt(canais)
    print(sbt)

    print("\n resultado exercício 10:")
    dia = ajustar_terca(dias)
    print(dia)

    print("\n resultado exercício 11:")
    numero = tres_primeiros(numeros)
    print(numero)

    print("\n resultado exercício 12:")
    arthur = remover_arthur(convidados)
    print(arthur)

    print("\n resultado exercício 13:")
    letra = inverter_lista(letras)
    print(letra)

    print("\n resultado exercício 14:")
    ponto = ordenar_pontos(pontos)
    print(ponto)

    print("\n resultado exercício 15:")
    valor = soma_extremos(valores)
    print(valor)

    print("\n resultado exercício 16:")
    ingrediente = tem_chocolate(ingredientes)
    print(ingrediente)

    print("\n resultado exercício 17:")
    amigos = juntar_amigos(amigos_escola, amigos_bairro)
    print(amigos)

    print("\n resultado exercício 18:")
    ano = ultimos_tres(anos)
    print(ano)

    print("\n resultado exercício 19:")
    brinquedo = remover_brinquedo_seguro(brinquedos, item='peteca')
    print(brinquedo)

    print("\n resultado exercício 20:")
    listar = trocar_extremos(lista)
    print(listar)