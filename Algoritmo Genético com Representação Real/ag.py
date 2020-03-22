from random import randint, uniform
from func_obj import func_obj

class Individuo():
    def __init__(self, genes):
        self.genes = genes
        self.fitness = None

class AG():
    def __init__(self, tam_populacao, num_geracoes, taxa_mutacao, num_genes, xmin, xmax, alpha, beta):
        self.tam_populacao = tam_populacao
        self.num_genes = num_genes
        self.xmin = xmin
        self.xmax = xmax
        self.alpha = alpha
        self.beta = beta
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

            pais.append(populacao[index-1])

        return pais


    def elitismo(self, populacao):
        # busca o melhor individuo da geração
        avaliacoes = []
        for ind in populacao:
            avaliacoes.append(abs(ind.fitness))

        val, idx = min((val, idx) for (idx, val) in enumerate(avaliacoes))

        return populacao[idx]

    def crossover(self, pais):
        # realiza o cruzamento entre dois individuos

        d = []
        filho1 = []
        filho2 = []
        i = 0
        cont = 0
        while i < self.tam_populacao:
            # print(type(pais[i]))
            d.append(abs(pais[i].fitness - pais[i+1].fitness))
            if (pais[i].fitness <= pais[i+1].fitness):
                # print(f"{pais[i].fitness} - {self.alpha} * {d[cont]}, {pais[i+1].fitness} + {self.beta} * {d[cont]}")
                filho1.append(uniform(pais[i].fitness - self.alpha * d[cont], pais[i+1].fitness + self.beta * d[cont]))
                filho2.append(uniform(pais[i].fitness - self.alpha * d[cont], pais[i+1].fitness + self.beta * d[cont]))
            else:
                filho1.append(uniform(pais[i+1].fitness - self.beta * d[cont], pais[i].fitness + self.alpha * d[cont]))
                filho2.append(uniform(pais[i+1].fitness - self.beta * d[cont], pais[i].fitness + self.alpha * d[cont]))
            cont += 1
            i += 2

        filhos = filho1 + filho2
        return filhos

        # if y.fitness > x.fitness:
        #     aux = y
        #     x = y
        #     y = aux

    def mutacao(self, populacao):
        # muta um bit aleatorio em uma taxa de 10% dos individuos aproximadamente
        for ind in populacao:
            if randint(0, 100) <= ag.taxa_mutacao:
                ind.genes[randint(0, 1)] = uniform(0, 1)


# (tam da população, numero de geracões, taxa mutação, numero de bits por individuo, xmin, xmax)
ag  = AG(50, 100, 10, 12, -2, 2, 0.75, 0.25)
ag.geraPopulacao()
nova_populacao = ag.defineIndividuos()

for geracao in range(ag.num_geracoes):

    ag.fitPopulacao(nova_populacao);
    melhorIndividuo = ag.elitismo(nova_populacao)

    pais = ag.roleta(nova_populacao)
    print(f"Melhor individuo da geração {geracao}\t  ->\tFitness: {melhorIndividuo.fitness}")

    nova_populacao = []
    filhos = ag.crossover(pais)
    nova_populacao = filhos

    nova_populacao.pop(randint(0, len(nova_populacao)-1))
    nova_populacao.append(melhorIndividuo)
    ag.mutacao(nova_populacao)
