from random import randint
from func_obj import func_obj

class Individuo():
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
        self.avaliacao = None

class AG():
    def __init__(self, tam_populacao, nbits):
        self.tam_populacao = tam_populacao
        self.nbits = nbits
        self.populacao = None

    def geraPopulacao(self):
        # gera a populacao de individuos em binarios de 12 bits
        ag.populacao = [[randint(0, 1) for x in range(self.nbits)] for y in range(self.tam_populacao)]

    def defineGenes(self):

        parametro1 = []
        parametro2 = []

        # divide o binario de cada individuo em 2 genes
        for individuo in ag.populacao:
            parametro1.append(individuo[:6])
            parametro2.append(individuo[6:])

        genes_individuos = []

        # converte os genes binarios em float
        for p1, p2 in zip(parametro1, parametro2):
            x1 = (float(int(''.join(str(e) for e in p1), 2)))
            x2 = (float(int(''.join(str(e) for e in p2), 2)))
            genes_individuos.append([x1, x2])

        return genes_individuos

    def avaliaPopulacao(self):
        # aplica a função objetivo para cada individuo da população
        for ind in individuo:
            ind.avaliacao = func_obj([ind.x1, ind.x2])

    def torneio(self):
        # 2 individuos duelam, o que possui a maior avaliação na Fo "permanece"
        individuo1 = individuo[randint(0, len(individuo) -1)]
        individuo2 = individuo[randint(0, len(individuo) -1)]
        if individuo1.avaliacao >= individuo2.avaliacao:
            vencedor = individuo1
        else:
            vencedor = individuo2
        individuo.remove(individuo1)
        individuo.remove(individuo2)
        return vencedor

ag  = AG(50, 12)
ag.geraPopulacao();
genes_individuos = ag.defineGenes();

individuo = []
for genes in genes_individuos:
    individuo.append(Individuo(genes[0], genes[1]))

ag.avaliaPopulacao();

nova_geracao = []
while len(nova_geracao) < ag.tam_populacao:
    pai = ag.torneio()
    mae = ag.torneio()
