from sys import argv
from AG import *
from Mochila import *
from utils import *

if len(argv) < 2:
    instancia = '05'
else:
    instancia = argv[1] # instancia vinda por terminal
    
(c, p, u, s) = leArquivos(instancia)
qtd_obj = quantidadeObjetos(p)
mochila = Mochila(qtd_obj, c, p, u, s)

solucao_otima = [-1, -1]
# AG(tam da população, numero de geracões, taxa mutação, taxa_cruzamento, probabilidade de vitória, numero de bits por individuo, com ou sem elitismo)
ag  = AG(100, 100, 10, 100, 90, qtd_obj, True)
nova_populacao = ag.geraPopulacao()

for geracao in range(ag.num_geracoes):
    ag.avaliaPopulacao(nova_populacao, mochila)
    melhorIndividuo = ag.getMelhorIndividuo(nova_populacao)

    if melhorIndividuo.solucao == mochila.solucao_otima and solucao_otima[0] == -1:
        solucao_otima = [geracao, melhorIndividuo.fitness] 

    print(f"Melhor individuo da geração {geracao}\t  →\tFitness: {melhorIndividuo.fitness}\tViavel? {melhorIndividuo.viavel}\tSolucão: {melhorIndividuo.solucao}]")

    populacao_atual = nova_populacao
    nova_populacao = []

    while len(nova_populacao) < ag.tam_populacao:
        pai = ag.selecao(populacao_atual, nova_populacao)
        filhos = ag.crossover(pai[0], pai[1])
        nova_populacao.extend(filhos)  
    
    ag.mutacao(nova_populacao)
    
    if (ag.elitismo):
        individuo_aleatorio = randint(0, len(nova_populacao)-1)  # sorteia um individuo
        nova_populacao[individuo_aleatorio] = melhorIndividuo    # substitui individuo sorteado pelo melhor individuo

if (solucao_otima[0] != -1):    
    print(f'O algoritmo genético encontrou a solução ótima ({solucao_otima[1]}) na geração {solucao_otima[0]}.')  
else:
    print(f'Não foi encontrada a solução ótima {mochila.solucao_otima}.')