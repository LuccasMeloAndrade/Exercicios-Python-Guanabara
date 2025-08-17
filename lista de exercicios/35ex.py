print("-=-" * 17)
print("Analisador de Triângulo")
print("-=-" * 17)

a = float(input("Medida do primeiro lado: "))
b = float(input("Medida do segundo lado: "))
c = float(input("Medida do terceiro lado: "))

if a + b > c and a + c > b and b + c > a:
    print("Os segmentos acima PODEM formar um triângulo")
else:
    print("Os segmentos acima NÃO PODEM formar um triângulo")