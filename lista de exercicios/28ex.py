import random
import time

print('-=' * 23)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print('-=' * 23)

n = int(input("Em que número eu pensei? "))
print("processando...")
time.sleep(1)

adv = random.randint(0, 5)

if n == adv:
    print("PARABÉNS, Você conseguiu me vencer!")
else:
    print(f"GANHEI, Eu pensei no número {adv} e não no {n}!")    