ano = int(input("Ano de nascimento: "))
idade = 2025 - ano
print(f"Quem nasceu em {ano} tem {idade} em 2025.")

if idade < 18:
    print(f"Ainda faltam {18 - idade} para o alistamento")
    print(f"Seu alistamento será em {2025 + (18 - idade)}.")
elif idade == 18:
    print("Você tem que se alistar esse ano!!!")
else:
    print(f"Você já deveria ter se alistado há {idade - 18} anos.")
    print(f"Seu alistamento foi em {2025 - (idade - 18)}")

