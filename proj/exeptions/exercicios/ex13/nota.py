def adicionar_nota_aluno(lista_notas: list, nova_nota: float):
    if 0.0 > nova_nota or nova_nota > 10.0:
        raise ValueError('A nota deve estar entre 0.0 e 10.0')
    
    if not isinstance(nova_nota, float):
        raise TypeError('Tipo incorreto')
    else:
        return lista_notas.append(nova_nota)