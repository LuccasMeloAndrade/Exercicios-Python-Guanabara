sal = float(input("Qual é o salário do funcionário: "))
if sal > 1250:
    print(f"O novo salário será de {sal * 1.1:.2f}")
else:
    print(f"O novo salário será de {sal * 1.15:.2f}")
