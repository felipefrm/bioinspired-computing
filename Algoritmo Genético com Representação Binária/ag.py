from random import randint, sample, random
from func_obj import func_obj

class Individuo():
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
        self.fitness = None

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
        # ajusta os parametros para o escopo do campo de busca
        x1_float = float(int(''.join(str(e) for e in individuo.x1), 2))
        x1 = ag.xmin + ((ag.xmax - ag.xmin)/(pow(2, ag.nbits/2)-1))*x1_float
        x2_float = float(int(''.join(str(e) for e in individuo.x2), 2))
        x2 = ag.xmin + ((ag.xmax - ag.xmin)/(pow(2, ag.nbits/2)-1))*x2_float

        return [x1, x2]

    def avaliaPopulacao(self, populacao):
        # aplica a função objetivo para cada individuo da população convertendo o binario em float
        for ind in populacao:
            parametro = ag.ajustaParametros(ind)
            ind.fitness = func_obj([parametro[0], parametro[1]])

    def torneio(self, populacao):
        # o ultimo individuo não terá adversário, logo é automaticamente escolhido
        if len(populacao) == 1:
            vencedor = populacao[0]
            populacao.remove(populacao[0])
            return vencedor

        # 2 individuos duelam, o que possui a maior avaliação na Fo tem 90% de chance vencer o duelo
        pv = 0.9    # probabilidade de vitória
        r = random() 

        sorteio = sample(range(len(populacao)), 2)  # sorteia 2 numeros aleatorios distintos
        individuo1 = populacao[sorteio[0]]
        individuo2 = populacao[sorteio[1]]
        
        if individuo1.fitness >= individuo2.fitness:
            vencedor = individuo1
            if (r < pv):
                vencedor = individuo2
            populacao.remove(vencedor)
        
        else:
            vencedor = individuo2
            if (r < pv):
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

    def crossover(self, pai, mae):
        # realiza o cruzamento entre dois individuos
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
        # muta um bit aleatorio em uma taxa de 10% dos individuos aproximadamente
        for ind in populacao:
            if randint(0,100) <= ag.taxa_mutacao:
                ind_bin = ind.x1 + ind.x2
                bit = randint(0, self.nbits-1)
                ind_bin[bit] = abs(int(ind_bin[bit]) - 1)
                ind.x1 = ind_bin[:6]
                ind.x2 = ind_bin[6:]


# AG(tam da população, numero de geracões, taxa mutação, numero de bits por individuo, xmin, xmax)
ag  = AG(50, 100, 10, 12, -2, 2)
ag.geraPopulacao()
nova_populacao = ag.defineIndividuos()

for geracao in range(ag.num_geracoes):
    ag.avaliaPopulacao(nova_populacao)
    melhorIndividuo = ag.elitismo(nova_populacao)

    [x1, x2] = ag.ajustaParametros(melhorIndividuo)

    print(f"Melhor individuo da geração {geracao}\t  →\tFitness: {melhorIndividuo.fitness}\t[x1: {x1}, x2: {x2}]")

    antiga_populacao = nova_populacao
    nova_populacao = []
    
    while len(nova_populacao) < ag.tam_populacao:
        pai = ag.torneio(antiga_populacao)
        mae = ag.torneio(antiga_populacao)
        filhos = ag.crossover(pai, mae)
        nova_populacao.extend(filhos)   # com excessão do melhor individuo, a nova população é totalmente composta novos individuos
    
    individuo_aleatorio = randint(0, len(nova_populacao)-1)  # sorteia um individuo
    nova_populacao[individuo_aleatorio] = melhorIndividuo    # substitui individuo sorteado pelo melhor individuo
    ag.mutacao(nova_populacao)
