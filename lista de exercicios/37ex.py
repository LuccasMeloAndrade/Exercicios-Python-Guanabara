n = int(input("Digite um número inteiro: "))

while True:
    print("Escolha uma das bases para a conversão:")
    print("[ 1 ] converter para BINÁRIO")
    print("[ 2 ] converter para OCTAL")
    print("[ 3 ] converter para HEXADECIMAL")
    escolha = int(input("Sua opção:"))

    if escolha == 1:
        print(f"{n} convertido para BINÁRIO é igual a {bin(n)[2:]}")
        break
    elif escolha == 2:
        print(f"{n} convertido para OCTAL é igual a {oct(n)[2:]}")
        break
    elif escolha == 3:
        print(f"{n} convertido para HEXADECIMAL é igual a {hex(n)[2:]}")
        break 
    else:
        print("⚠ Escolha inválida, tente novamente")   
    
