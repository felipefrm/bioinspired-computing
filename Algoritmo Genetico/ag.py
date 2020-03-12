from random import randint, sample
from func_obj import func_obj

class Individuo():
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
        self.avaliacao = None

class AG():
    def __init__(self, tam_populacao, num_geracoes, taxa_mutacao, nbits, xmin, xmax):
        self.tam_populacao = tam_populacao
        self.nbits = nbits
        self.xmin = xmin
        self.xmax = xmax
        self.populacao = None
        self.num_geracoes = num_geracoes
        self.taxa_mutacao = taxa_mutacao

    def geraPopulacao(self):
        # gera a populacao de individuos em binarios de 12 bits
        ag.populacao = [[randint(0, 1) for x in range(self.nbits)] for y in range(self.tam_populacao)]


    def defineIndividuos(self):

        # divide o binario de cada individuo em 2 genes
        individuo = []
        for ind in ag.populacao:
            individuo.append(Individuo(ind[:6], ind[6:]))

        return individuo

    def ajustaParametros(self, individuo):

        x1_float = float(int(''.join(str(e) for e in individuo.x1), 2))
        # print("sem ajuste", x1_float)
        x1 = ag.xmin + ((ag.xmax - ag.xmin)/(pow(2, ag.nbits)-1))*x1_float
        # print(f"{ag.xmin} + ({ag.xmax - ag.xmin})/(2^{ag.nbits}-1) * {x1_float}")
        # print("com ajuste", x1)

        x2_float = float(int(''.join(str(e) for e in individuo.x2), 2))
        x2 = ag.xmin + ((ag.xmax - ag.xmin)/(pow(2, ag.nbits)-1))*x2_float

        return [x1, x2]

    def avaliaPopulacao(self, populacao):
        # aplica a função objetivo para cada individuo da população convertendo o binario em float
        for ind in populacao:
            parametro = ag.ajustaParametros(ind)
            # print(parametro[0])
            # print(parametro[1])

            ind.avaliacao = func_obj([parametro[0], parametro[1]])

    def torneio(self, populacao):

        # o ultimo individuo não terá adversário, logo é automaticamente escolhido
        if len(populacao) == 1:
            vencedor = populacao[0]
            populacao.remove(populacao[0])
            # print("sou o ultimo")
            return vencedor

        # 2 individuos duelam, o que possui a maior avaliação na Fo "permanece"
        # print(f"sample: {range(len(populacao))}")
        sorteio = sample(range(len(populacao)), 2)
        individuo1 = populacao[sorteio[0]]
        # print("peguei o individuo ", sorteio[0])
        individuo2 = populacao[sorteio[1]]
        # print("peguei o individuo ", sorteio[1])
        if individuo1.avaliacao >= individuo2.avaliacao:
            vencedor = individuo1
            populacao.remove(individuo1)
        else:
            vencedor = individuo2
            populacao.remove(individuo2)
        return vencedor

    def elitismo(self, populacao):
        avaliacoes = []
        for ind in populacao:
            avaliacoes.append(ind.avaliacao)

        val, idx = min((val, idx) for (idx, val) in enumerate(avaliacoes))

        return populacao[idx]

    def crossover(self, pai, mae):

        pai_bin = pai.x1 + pai.x2
        mae_bin = mae.x1 + mae.x2

        corte = randint(0, ag.nbits)

        filhos = []

        filho1_bin = pai_bin[:corte] + mae_bin[corte:]
        filho1 = Individuo(filho1_bin[:6], filho1_bin[6:])
        filhos.append(filho1)

        filho2_bin = mae_bin[:corte] + pai_bin[corte:]
        filho2 = Individuo(filho2_bin[:6], filho2_bin[6:])
        filhos.append(filho2)

        return filhos

    def mutacao(self, populacao):

        for ind in populacao:
            if randint(0,100) <= ag.taxa_mutacao:
                ind_bin = ind.x1 + ind.x2
                # print("Antes  ", ind_bin)
                bit = randint(0, self.nbits-1)
                # print(f"vou mudar o bit {bit}")
                # print(f"transformar {ind_bin[bit]} em {abs(int(ind_bin[bit]) - 1)}")
                ind_bin[bit] = abs(int(ind_bin[bit]) - 1)
                ind.x1 = ind_bin[:6]
                ind.x2 = ind_bin[6:]
                # print("depois ", ind.x1 + ind.x2)

ag  = AG(50, 100, 10, 12, -2, 2)
ag.geraPopulacao()
nova_populacao = ag.defineIndividuos()
# print(nova_populacao[0].x1 + nova_populacao[0].x2)



for geracao in range(ag.num_geracoes):
    # print("Passei")
    ag.avaliaPopulacao(nova_populacao);
    melhorIndividuo = ag.elitismo(nova_populacao)
    print(f"Melhor individuo da geração {geracao} -> avaliação: {melhorIndividuo.avaliacao}")

    antiga_populacao = nova_populacao
    nova_populacao = []
    while len(nova_populacao) < ag.tam_populacao:
        pai = ag.torneio(antiga_populacao)
        mae = ag.torneio(antiga_populacao)
        filhos = ag.crossover(pai, mae)
        nova_populacao.extend(filhos)

    # print("POP ", len(nova_populacao))
    nova_populacao.pop(randint(0, len(nova_populacao)-1))
    nova_populacao.append(melhorIndividuo)
    ag.mutacao(nova_populacao)
