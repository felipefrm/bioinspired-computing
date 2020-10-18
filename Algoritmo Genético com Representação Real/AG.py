from Individuo import Individuo
from random import randint, uniform
from func_obj import func_obj

class AG():
    def __init__(self, tam_populacao, num_geracoes, taxa_mutacao, taxa_cruzamento, num_genes, xmin, xmax, alpha, beta):
        self.tam_populacao = tam_populacao
        self.num_genes = num_genes
        self.xmin = xmin
        self.xmax = xmax
        self.alpha = alpha
        self.beta = beta
        self.num_geracoes = num_geracoes
        self.taxa_mutacao = taxa_mutacao
        self.taxa_cruzamento = taxa_cruzamento

    def geraPopulacao(self):
        populacao = [[uniform(self.xmin, self.xmax) for x in range(self.num_genes)] for y in range(self.tam_populacao)]
        return populacao

    def defineIndividuos(self, populacao):
        individuo = []
        for ind in populacao:
            individuo.append(Individuo([ind[0], ind[1]]))

        return individuo

    def fitPopulacao(self, populacao):
        # aplica a função objetivo para cada individuo da população
        for ind in populacao:
            ind.fitness = func_obj([ind.genes[0], ind.genes[1]])

    def roleta(self, populacao):

        fit_total = sum(abs(1/ind.fitness) for ind in populacao)
        
        roleta = []
        for ind in populacao:
            roleta.append((abs(1/ind.fitness))/fit_total)
    
        # roleta.sort(reverse=False)

        pais = []
        for i in range(self.tam_populacao):

            r = uniform(0, 1)
            acumulador = index = 0
            while (acumulador < r):
                acumulador += roleta[index]
                index += 1

            pais.append(populacao[index-1])

        return pais


    def getMelhorIndividuo(self, populacao):
        # busca o melhor individuo da geração
        fitness = []
        for ind in populacao:
            fitness.append(abs(ind.fitness))

        val, idx = min((val, idx) for (idx, val) in enumerate(fitness))

        return populacao[idx]

    def getPiorIndividuo(self, populacao):
        # busca o pior individuo da geração
        fitness = []
        for ind in populacao:
            fitness.append(abs(ind.fitness))

        val, idx = max((val, idx) for (idx, val) in enumerate(fitness))

        return populacao[idx]

    def getMediaIndividuos(self, populacao):    
        fit_total = sum(abs(ind.fitness) for ind in populacao)
        return fit_total/len(populacao)

    def crossover(self, pais, algoritmo='alpha'):

        d = []
        filhos = []
        filho1 = []
        filho2 = []
        cont = 0

        if algoritmo == 'alpha':
            
            while cont < self.tam_populacao:
                pai1 = pais[cont]                       
                pai2 = pais[cont+1]
                filho1.clear()
                filho2.clear()

                if randint(0, 100) <= self.taxa_cruzamento: # realiza o cruzamento entre dois individuos 
                                                            # gerando dois novos individuos
                    for i in range(self.num_genes):         
                        d.append(abs(pai1.genes[i] - pai2.genes[i]))
                        filho1.append(uniform(min(pai1.genes[i], pai2.genes[i]) - self.alpha * d[i], max(pai1.genes[i], pai2.genes[i] + self.alpha * d[i])))
                        filho2.append(uniform(min(pai1.genes[i], pai2.genes[i]) - self.alpha * d[i], max(pai1.genes[i], pai2.genes[i] + self.alpha * d[i])))                   

                        self.checkEspacoBusca(filho1[i])
                        self.checkEspacoBusca(filho2[i])

                    filhos.extend([Individuo(filho1), Individuo(filho2)])
                                    
                else: # os pais vão para a próxima geração
                    filhos.extend([pai1, pai2])
                
                cont += 2


        elif algoritmo == 'alphabeta':

            while cont < self.tam_populacao:
                pai1 = pais[cont]
                pai2 = pais[cont+1]

                if randint(0, 100) <= self.taxa_cruzamento: # realiza o cruzamento entre dois individuos 
            
                    if (pai1.fitness < pai2.fitness): # se pai1 nao for melhor que pa2, troca pai1 com pai2
                        pai1, pai2 = pai2, pai1
            
                    for i in range(self.num_genes):         
                        d.append(abs(pai1.genes[i] - pai2.genes[i]))

                        if pai1.genes[i] <= pai2.genes[i]:
                            filho1.append(uniform(pai1.genes[i] - self.alpha * d[i], pai2.genes[i] + self.beta * d[i]))
                            filho2.append(uniform(pai1.genes[i] - self.alpha * d[i], pai2.genes[i] + self.beta * d[i]))

                        else:
                            filho1.append(uniform(pai2.genes[i] - self.beta * d[i], pai1.genes[i] + self.alpha * d[i]))
                            filho2.append(uniform(pai2.genes[i] - self.beta * d[i], pai1.genes[i] + self.alpha * d[i]))

                        self.checkEspacoBusca(filho1[i], self.xmin, self.xmax)
                        self.checkEspacoBusca(filho2[i], self.xmin, self.xmax)

                    filhos.extend([Individuo(filho1), Individuo(filho2)])

                else:
                    filhos.extend([pai1, pai2])

                cont += 2
        
        return filhos

    def checkEspacoBusca(self, x):
        if x < self.xmin:
            return self.xmin
        elif x > self.xmax:
            return self.xmax
        return x

    def mutacao(self, populacao):
        for ind in populacao:
            if randint(0,100) <= self.taxa_mutacao:
                indice = randint(0, 1)
                ind.genes[indice] = uniform(self.xmin, self.xmax)
