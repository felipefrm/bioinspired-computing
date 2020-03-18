from random import randint, uniform
from func_obj import func_obj

class Individuo():
    def __init__(self, genes):
        self.genes = genes
        self.fitness = None

class AG():
    def __init__(self, tam_populacao, num_geracoes, taxa_mutacao, num_genes, xmin, xmax):
        self.tam_populacao = tam_populacao
        self.num_genes = num_genes
        self.xmin = xmin
        self.xmax = xmax
        self.populacao = None
        self.num_geracoes = num_geracoes
        self.taxa_mutacao = taxa_mutacao

    def geraPopulacao(self):

        ag.populacao = [[uniform(self.xmin, self.xmax) for x in range(self.num_genes)] for y in range(self.tam_populacao)]


    def defineIndividuos(self):

        individuo = []
        for ind in ag.populacao:
            individuo.append(Individuo([ind[0], ind[1]]))

        return individuo

    def fitPopulacao(self, populacao):
        # aplica a função objetivo para cada individuo da população convertendo o binario em float
        for ind in populacao:
            ind.fitness = func_obj([ind.genes[0], ind.genes[1]])

    def roleta(self, populacao):

        fit_total = sum(ind.fitness for ind in populacao)

        roleta = []
        for ind in populacao:
            roleta.append(ind.fitness/fit_total)

        pais = []
        for i in range(self.tam_populacao):

            r = uniform(0, 1)

            acumulador = index = 0
            while (acumulador < r):
                acumulador += roleta[index]
                index += 1

            pais.append(roleta[index-1])

        return pais


    def elitismo(self, populacao):
        # busca o melhor individuo da geração
        avaliacoes = []
        for ind in populacao:
            avaliacoes.append(abs(ind.fitness))

        val, idx = min((val, idx) for (idx, val) in enumerate(avaliacoes))

        return populacao[idx]

    def crossover(self, x, y):
        # realiza o cruzamento entre dois individuos

        if y.fitness > x.fitness:
            aux = y
            x = y
            y = aux

            # NOT TERMINATED

        return filhos

    def mutacao(self, populacao):
        # muta um bit aleatorio em uma taxa de 10% dos individuos aproximadamente
        for ind in populacao:
            if randint(0, 100) <= ag.taxa_mutacao:
                ind.genes[randint(0, 1)] = uniform(0, 1)


# (tam da população, numero de geracões, taxa mutação, numero de bits por individuo, xmin, xmax)
ag  = AG(50, 100, 10, 12, -2, 2)
ag.geraPopulacao()
nova_populacao = ag.defineIndividuos()

for geracao in range(ag.num_geracoes):

    ag.fitPopulacao(nova_populacao);
    melhorIndividuo = ag.elitismo(nova_populacao)

    pais = ag.roleta(nova_populacao)

    print(f"Melhor individuo da geração {geracao}\t  ->\tFitness: {melhorIndividuo.fitness}")

    nova_populacao = []
    while len(nova_populacao) < ag.tam_populacao:
        filhos = ag.crossover(pais[len(nova_populacao)], pais[len(nova_populacao)+1])
        nova_populacao.extend(filhos)

    nova_populacao.pop(randint(0, len(nova_populacao)-1))
    nova_populacao.append(melhorIndividuo)
    ag.mutacao(nova_populacao)
