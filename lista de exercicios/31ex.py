km = float(input("Distancia da viagem: "))
if km <= 200:
    passagem = km * 0.5
    print(f"Você está prestes a começar uma viagem de {km}Km\n E o preço da sua passagem será de R${passagem}")
else:
    passagem = km * 0.45
    print(f"Você está prestes a começar uma viagem de {km}Km\n E o preço da sua passagem será de R${passagem}")    