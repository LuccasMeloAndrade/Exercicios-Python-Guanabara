import random 
lista = []
for i in range(1, 5):
    aluno = input(f'{i}º Aluno: ')
    lista.append(aluno)
print(f'Lista completa: {lista}')
print(f'O aluno escolhido foi {random.choice(lista)}')    