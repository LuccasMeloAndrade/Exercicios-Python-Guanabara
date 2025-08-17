import random
lista = []
for i in range(1, 5):
    aluno = input(f'{i}º Aluno: ')
    lista.append(aluno)
sorteio = int(input('Quantos alunos quer sortear: '))    
print(f'Lista completa: {lista}')
print(f'A ordem de apresentação será {random.sample(lista, sorteio)}')