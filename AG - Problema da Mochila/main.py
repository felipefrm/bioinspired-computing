from AG import *
from Mochila import *
from utils import *

(c, p, u, s) = leArquivos("01")
qtd_obj = quantidadeObjetos(p)
mochila = Mochila(qtd_obj, c, p, u, s)

# AG(tam da população, numero de geracões, taxa mutação, taxa_cruzamento, probabilidade de vitória, numero de bits por individuo)
ag  = AG(50, 100, 10, 100, 90, qtd_obj)
nova_populacao = ag.geraPopulacao()

for geracao in range(ag.num_geracoes):
    ag.avaliaPopulacao(nova_populacao, mochila)
    melhorIndividuo = ag.elitismo(nova_populacao)

    print(f"Melhor individuo da geração {geracao}\t  →\tFitness: {melhorIndividuo.fitness}\tSolucão: {melhorIndividuo.solucao}]")

    antiga_populacao = nova_populacao
    nova_populacao = []
    
    while len(nova_populacao) < ag.tam_populacao:
        pai1 = ag.torneio(antiga_populacao)
        pai2 = ag.torneio(antiga_populacao)
        filhos = ag.crossover(pai1, pai2)
        nova_populacao.extend(filhos)   # com excessão do melhor individuo, a nova população é totalmente composta novos individuos
    
    individuo_aleatorio = randint(0, len(nova_populacao)-1)  # sorteia um individuo
    nova_populacao[individuo_aleatorio] = melhorIndividuo    # substitui individuo sorteado pelo melhor individuo
    ag.mutacao(nova_populacao)
