# AG(tamanho da populacao, numero de geracoes, taxa de mutacao, taxa de cruzamento, numero de genes, xmin, xmax, alpha, beta)
from AG import *

ag  = AG(50, 100, 10, 100, 2, -2, 2, 0.5, 0.25)
populacao_inicial = ag.geraPopulacao()
populacao_atual = ag.defineIndividuos(populacao_inicial)

for geracao in range(ag.num_geracoes):

    ag.fitPopulacao(populacao_atual)
    melhorIndividuo = ag.elitismo(populacao_atual)

    pais = ag.roleta(populacao_atual)
    print(f"Melhor individuo da geração {geracao}\t  ->\tFitness: {melhorIndividuo.fitness}")

    populacao_atual = []
    filhos = ag.crossover(pais, 'alpha')
    populacao_atual = filhos

    ag.mutacao(populacao_atual)
    populacao_atual.pop(randint(0, len(populacao_atual)-1))
    populacao_atual.append(melhorIndividuo)
