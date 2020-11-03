from random import randint, sample, random, uniform
from Individuo import Individuo
from func_obj import func_obj

class AG():
    def __init__(self, tam_populacao, num_geracoes, taxa_mutacao, taxa_cruzamento, prob_vitoria, nbits, elitismo):
        self.tam_populacao = tam_populacao
        self.nbits = nbits
        self.populacao = None
        self.num_geracoes = num_geracoes
        self.taxa_mutacao = taxa_mutacao
        self.taxa_cruzamento = taxa_cruzamento
        self.prob_vitoria = prob_vitoria
        self.elitismo = elitismo

    def geraPopulacao(self):
        # gera a populacao de individuos em binarios de nbits
        self.populacao = [[randint(0, 1) for x in range(self.nbits)] for y in range(self.tam_populacao)]
        individuo = []
        for ind in self.populacao:
            individuo.append(Individuo(ind))
        return individuo

    def avaliaPopulacao(self, populacao, mochila):
        # aplica a função objetivo para cada individuo da população convertendo o binario em float
        for ind in populacao:
            (ind.fitness, ind.viavel) = func_obj(ind.solucao, mochila)

    def roleta(self, populacao):

        fit_total = sum(ind.fitness for ind in populacao)
        
        roleta = []
        for ind in populacao:
            roleta.append(ind.fitness/fit_total)

        pais = []

        for i in range(self.tam_populacao):
            print(roleta[i])
            r = uniform(0, 1)
            acumulador = index = 0
            while (acumulador < r):
                acumulador += roleta[index]
                index += 1

            pais.append(populacao[index-1])

        print(sum(roleta), "\n")

        return pais
        

    def torneio(self, populacao):
        # o ultimo individuo não terá adversário, logo é automaticamente escolhido
        if len(populacao) == 1:
            vencedor = populacao[0]
            populacao.remove(populacao[0])
            return vencedor

        sorteio = sample(range(len(populacao)), 2)  # sorteia 2 numeros aleatorios distintos
        individuo1 = populacao[sorteio[0]]
        individuo2 = populacao[sorteio[1]]

        # 2 individuos duelam, o que possui a maior avaliação na Fo tem maior de chance vencer o duelo
        # o fator de probabilidade de vitória está guardada no atributo "prob_vitoria" da classe self
        r = randint(0, 100)

        if individuo1.fitness >= individuo2.fitness:
            vencedor = individuo1
            if (r >= self.prob_vitoria):
                vencedor = individuo2
            populacao.remove(vencedor)
        
        else:
            vencedor = individuo2
            if (r >= self.prob_vitoria):
                vencedor = individuo1
            populacao.remove(vencedor)

        return vencedor

    def getMelhorIndividuo(self, populacao):
        # busca o melhor individuo da geração
        avaliacoes = []
        for ind in populacao:
            avaliacoes.append(ind.fitness)

        val, idx = max((val, idx) for (idx, val) in enumerate(avaliacoes))
        melhorIndividuo = populacao[idx]     # salva o melhor individuo, independente se é viavel ou não

        for i in range(self.tam_populacao):
            val, idx = max((val, idx) for (idx, val) in enumerate(avaliacoes))
            if populacao[idx].viavel:
                melhorIndividuo = populacao[idx]    # salva o melhor individuo viavel, se existir
                break
            avaliacoes[idx] = 0

        return melhorIndividuo

    def getPiorIndividuo(self, populacao):
        # busca o pior individuo da geração
        fitness = []
        for ind in populacao:
            fitness.append(ind.fitness)

        val, idx = min((val, idx) for (idx, val) in enumerate(fitness))

        return populacao[idx]

    def getMediaIndividuos(self, populacao):    
        fit_total = sum(ind.fitness for ind in populacao)
        return fit_total/len(populacao)


    def crossover(self, pai1, pai2):

        if randint(0, 100) <= self.taxa_cruzamento:
            # realiza o cruzamento entre dois individuos
            corte = randint(0, self.nbits)

            filhos = []

            filho1_s = pai1.solucao[:corte] + pai2.solucao[corte:]
            filho1 = Individuo(filho1_s)
            filhos.append(filho1)

            filho2_s = pai2.solucao[:corte] + pai1.solucao[corte:]
            filho2 = Individuo(filho2_s)
            filhos.append(filho2)
            
            return filhos

        else:
            return [pai1, pai2]


    def mutacao(self, populacao):
        # muta um bit aleatorio 
        for ind in populacao:
            if randint(0,100) <= self.taxa_mutacao:
                bit = randint(0, self.nbits-1)
                ind.solucao[bit] = abs(int(ind.solucao[bit]) - 1)
