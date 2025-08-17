lista = []
for i in range(1, 4):
    n = float(input(f"{i}º número: "))
    lista.append(n)
print(f"O maior é {max(lista)} e o menor é {min(lista)}")