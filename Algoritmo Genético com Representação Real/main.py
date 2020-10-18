# from sys import argv

from utils import fileOperations
from AG import *

# AG(tamanho da populacao, numero de geracoes, taxa de mutacao, taxa de cruzamento, numero de genes, xmin, xmax, alpha, beta)
ag  = AG(50, 100, 10, 100, 2, -2, 2, 0.75, 0.25)
populacao_inicial = ag.geraPopulacao()
populacao_atual = ag.defineIndividuos(populacao_inicial)

melhorIndividuo = []
piorIndividuo = []
mediaIndividuos = []

for geracao in range(ag.num_geracoes):

    ag.fitPopulacao(populacao_atual)
    melhorIndividuo.append(ag.getMelhorIndividuo(populacao_atual))
    piorIndividuo.append(ag.getPiorIndividuo(populacao_atual))
    mediaIndividuos.append(ag.getMediaIndividuos(populacao_atual))

    pais = ag.roleta(populacao_atual)

    print(f"Melhor individuo da geração {geracao}\t  ->\tFitness: {melhorIndividuo[geracao].fitness}")
    print(f"Pior individuo da geração {geracao}\t  ->\tFitness: {piorIndividuo[geracao].fitness}")
    print(f"Media da geração {geracao}\t\t  ->\tFitness: {mediaIndividuos[geracao]}\n")
    
    populacao_atual = []
    filhos = ag.crossover(pais, 'alphabeta')
    populacao_atual = filhos

    ag.mutacao(populacao_atual)
    populacao_atual.pop(randint(0, len(populacao_atual)-1))
    populacao_atual.append(melhorIndividuo[geracao])

fileOperations(melhorIndividuo, piorIndividuo, mediaIndividuos, ag.taxa_mutacao, ag.taxa_cruzamento, ag.tam_populacao, ag.num_geracoes)