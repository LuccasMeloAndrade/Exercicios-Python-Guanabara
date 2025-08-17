casa = float(input("Valor da casa: "))
salario = float(input("Qual é o seu salário: "))
anos = float(input("Quantos anos irá pagar: "))

prestacao = casa / (anos * 12)

if prestacao > (salario * 0.3):
    print(f"Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação sera de R${prestacao:.2f}")
    print("Empréstimo NEGADO!")
else:
    print(f"Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação sera de R${prestacao:.2f}")
    print("Empréstimo pode ser CONCEDIDO!")
