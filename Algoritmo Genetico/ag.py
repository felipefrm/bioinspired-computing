
from random import randint

tamanho_populacao = 50
nbits = 12

# gera a populacao de individuos em binarios de 12 bits
populacao = [[randint(0, 1) for x in range(nbits)] for y in range(tamanho_populacao)]

parametro1 = []
parametro2 = []

# divide o binario em 2 parametros
for ind in populacao:
    parametro1.append(ind[:6])
    parametro2.append(ind[6:])

x1 = []
x2 = []
# converte os parametros binarios em float
for p1, p2 in zip(parametro1, parametro2):
    x1.append(float(int(''.join(str(e) for e in p1), 2)))
    x2.append(float(int(''.join(str(e) for e in p2), 2)))
