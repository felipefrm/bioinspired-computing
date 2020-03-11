from random import randint, sample
from func_obj import func_obj

class Individuo():
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
        self.avaliacao = None

class AG():
    def __init__(self, tam_populacao, num_geracoes, nbits):
        self.tam_populacao = tam_populacao
        self.nbits = nbits
        self.populacao = None
        self.num_geracoes = num_geracoes

    def geraPopulacao(self):
        # gera a populacao de individuos em binarios de 12 bits
        ag.populacao = [[randint(0, 1) for x in range(self.nbits)] for y in range(self.tam_populacao)]


    def defineIndividuos(self):

        parametro2 = []
        parametro1 = []

        # divide o binario de cada individuo em 2 genes
        genes_individuos = []
        individuo = []
        # print(ag.populacao)
        for ind in ag.populacao:
            individuo.append(Individuo(ind[:6], ind[6:]))

        return individuo


    def avaliaPopulacao(self):
        # aplica a função objetivo para cada individuo da população
        print(individuo[0].x1 + individuo[0].x2)
        for ind in individuo:
            x1_float = float(int(''.join(str(e) for e in ind.x1), 2))
            x2_float = float(int(''.join(str(e) for e in ind.x2), 2))
            ind.avaliacao = func_obj([x1_float, x2_float])

    def torneio(self):

        # o ultimo individuo não terá adversário, logo é automaticamente escolhido
        if len(individuo) == 1:
            vencedor = individuo[0]
            individuo.remove(individuo[0])
            return vencedor

        # 2 individuos duelam, o que possui a maior avaliação na Fo "permanece"
        # print(f"sample: {range(len(individuo))}")
        sorteio = sample(range(len(individuo)), 2)
        individuo1 = individuo[sorteio[0]]
        # print("peguei o individuo ", sorteio[0])
        individuo2 = individuo[sorteio[1]]
        # print("peguei o individuo ", sorteio[1])
        if individuo1.avaliacao >= individuo2.avaliacao:
            vencedor = individuo1
            individuo.remove(individuo1)
        else:
            vencedor = individuo2
            individuo.remove(individuo2)
        return vencedor

    def elitismo(self):
        avaliacoes = []
        for ind in individuo:
            avaliacoes.append(ind.avaliacao)

        val, idx = min((val, idx) for (idx, val) in enumerate(avaliacoes))

        return individuo[idx]

    def crossover(self, pai, mae):

        pai_bin = pai.x1 + pai.x2
        mae_bin = mae.x1 + mae.x2

        corte = randint(0,12)

        filhos = []

        filho1_bin = pai_bin[:corte] + mae_bin[corte:]
        filho1 = Individuo(filho1_bin[:6], filho1_bin[6:])
        filhos.append(filho1)

        filho2_bin = mae_bin[:corte] + pai_bin[corte:]
        filho2 = Individuo(filho2_bin[:6], filho2_bin[6:])
        filhos.append(filho2)

        return filhos

    def mutacao(self):

        taxa_mutacao = 10
        for ind in individuo:
            if randint(0,100) <= taxa_mutacao:
                ind_bin = ind.x1 + ind.x2
                print("Antes ", ind_bin)
                bit = randint(0, self.nbits)
                ind_bin[bit] = abs(int(ind_bin[bit]) - 1)
                if bit > 6:
                    ind.x1 = ind_int[:6]
                else:
                    ind.x2 = ind_int[6:]
                print("depois ", ind.x1 + ind.x2)

ag  = AG(50, 100, 12)
ag.geraPopulacao()
individuo = ag.defineIndividuos()
print(individuo[0].x1 + individuo[0].x2)



for geracao in range(ag.num_geracoes):
    print("Passei")
    ag.avaliaPopulacao();
    melhorIndividuo = ag.elitismo()
    # print(f"Melhor individuo da geração {geracao} -> avaliação: {melhorIndividuo.avaliacao}")

    nova_populacao = []
    while len(nova_populacao) < ag.tam_populacao:
        pai = ag.torneio()
        mae = ag.torneio()
        filhos = ag.crossover(pai, mae)
        nova_populacao.extend(filhos)
        print("POP ", len(nova_populacao))

    nova_populacao.pop(randint(0, 50))
    nova_populacao.append(melhorIndividuo)
    ag.mutacao()
