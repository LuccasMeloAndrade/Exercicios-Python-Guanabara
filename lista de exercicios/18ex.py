import math
an = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tg = math.tan(math.radians(an))
print(f'O ângulo de {an} tem o SENO de {seno:.2f}')
print(f'O ângulo de {an} tem o COSSENO de {cos:.2f}')
print(f'O âmgulo de {an} tem a TANGENTE de {tg:.2f}')