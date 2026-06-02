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
    
