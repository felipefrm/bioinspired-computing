from AG import *

# AG(tam da população, numero de geracões, taxa mutação, taxa_cruzamento, probabilidade de vitória, numero de bits por individuo, xmin, xmax)
ag  = AG(50, 100, 10, 100, 90, 12, -2, 2)
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
        pai1 = ag.torneio(antiga_populacao)
        pai2 = ag.torneio(antiga_populacao)
        filhos = ag.crossover(pai1, pai2)
        nova_populacao.extend(filhos)   # com excessão do melhor individuo, a nova população é totalmente composta novos individuos
    
    individuo_aleatorio = randint(0, len(nova_populacao)-1)  # sorteia um individuo
    nova_populacao[individuo_aleatorio] = melhorIndividuo    # substitui individuo sorteado pelo melhor individuo
    ag.mutacao(nova_populacao)
