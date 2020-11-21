from random import randint, sample, random
from func_obj import func_obj
from Individuo import Individuo

class AG():
    def __init__(self, tam_populacao, num_geracoes, taxa_mutacao, taxa_cruzamento, prob_vitoria, nbits, xmin, xmax):
        self.tam_populacao = tam_populacao
        self.nbits = nbits
        self.xmin = xmin
        self.xmax = xmax
        self.populacao = None
        self.num_geracoes = num_geracoes
        self.taxa_mutacao = taxa_mutacao
        self.taxa_cruzamento = taxa_cruzamento
        self.prob_vitoria = prob_vitoria

    def geraPopulacao(self):
        # gera a populacao de individuos em binarios de 12 bits
        self.populacao = [[randint(0, 1) for x in range(self.nbits)] for y in range(self.tam_populacao)]


    def defineIndividuos(self):
        # divide o binario de cada individuo em 2 genes
        individuo = []
        for ind in self.populacao:
            individuo.append(Individuo(ind[:6], ind[6:]))

        return individuo

    def ajustaParametros(self, individuo):
        # ajusta os parametros para o escopo do campo de busca
        x1_float = float(int(''.join(str(e) for e in individuo.x1), 2))
        x1 = self.xmin + ((self.xmax - self.xmin)/(pow(2, self.nbits/2)-1))*x1_float
        x2_float = float(int(''.join(str(e) for e in individuo.x2), 2))
        x2 = self.xmin + ((self.xmax - self.xmin)/(pow(2, self.nbits/2)-1))*x2_float

        return [x1, x2]

    def avaliaPopulacao(self, populacao):
        # aplica a função objetivo para cada individuo da população convertendo o binario em float
        for ind in populacao:
            parametro = self.ajustaParametros(ind)
            ind.fitness = func_obj([parametro[0], parametro[1]])

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

    def elitismo(self, populacao):
        # busca o melhor individuo da geração
        avaliacoes = []
        for ind in populacao:
            avaliacoes.append(abs(ind.fitness))

        val, idx = min((val, idx) for (idx, val) in enumerate(avaliacoes))

        return populacao[idx]

    def crossover(self, pai1, pai2):

        if randint(0, 100) <= self.taxa_cruzamento:
            # realiza o cruzamento entre dois individuos
            pai1_bin = pai1.x1 + pai1.x2
            pai2_bin = pai2.x1 + pai2.x2

            corte = randint(0, self.nbits)

            filhos = []

            filho1_bin = pai1_bin[:corte] + pai2_bin[corte:]
            filho1 = Individuo(filho1_bin[:6], filho1_bin[6:])
            filhos.append(filho1)

            filho2_bin = pai2_bin[:corte] + pai1_bin[corte:]
            filho2 = Individuo(filho2_bin[:6], filho2_bin[6:])
            filhos.append(filho2)
            
            return filhos

        else:
            return [pai1, pai2]


    def mutacao(self, populacao):
        # muta um bit aleatorio em uma taxa de 10% dos individuos aproximadamente
        for ind in populacao:
            if randint(0,100) <= self.taxa_mutacao:
                ind_bin = ind.x1 + ind.x2
                bit = randint(0, self.nbits-1)
                ind_bin[bit] = abs(int(ind_bin[bit]) - 1)
                ind.x1 = ind_bin[:6]
                ind.x2 = ind_bin[6:]
