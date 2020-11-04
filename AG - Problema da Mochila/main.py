from sys import argv
from AG import *
from Mochila import *
from utils import *

if (len(argv) < 2):
    instancia = '05'
else:
    instancia = argv[1] # instancia vinda por terminal
    
(c, p, u, s) = leArquivos(instancia)
qtd_obj = quantidadeObjetos(p)
mochila = Mochila(qtd_obj, c, p, u, s)

# AG(tam da população, numero de geracões, taxa mutação, taxa_cruzamento, probabilidade de vitória, numero de bits por individuo, com ou sem elitismo)
ag  = AG(100, 100, 5, 100, 90, qtd_obj, True)
nova_populacao = ag.geraPopulacao()

for geracao in range(ag.num_geracoes):
    ag.avaliaPopulacao(nova_populacao, mochila)
    melhorIndividuo = ag.getMelhorIndividuo(nova_populacao)

    print(f"Melhor individuo da geração {geracao}\t  →\tFitness: {melhorIndividuo.fitness}\tViavel? {melhorIndividuo.viavel}\tSolucão: {melhorIndividuo.solucao}]")

    populacao_atual = nova_populacao
    nova_populacao = []

    # pais = ag.roleta(populacao_atual)
    # pais.append(pais[0])

    while len(nova_populacao) < ag.tam_populacao:
        pai1 = ag.torneio(populacao_atual)
        if (ag.tam_populacao % 2 != 0 and len(nova_populacao)+1 == ag.tam_populacao):
            pai2 = pai1     # caso o tamanho da populacao seja impar, na ultima iteração do while vai sobrar acontecer só 1 torneio
        else:               # entao, o pai2 será o mesmo que o pai1
            pai2 = ag.torneio(populacao_atual)

        filhos = ag.crossover(pai1, pai2)
        # filhos = ag.crossover(pais[len(nova_populacao)], pais[len(nova_populacao)+1])
        nova_populacao.extend(filhos)  
    
    ag.mutacao(nova_populacao)
    
    if (ag.elitismo):
        individuo_aleatorio = randint(0, len(nova_populacao)-1)  # sorteia um individuo
        nova_populacao[individuo_aleatorio] = melhorIndividuo    # substitui individuo sorteado pelo melhor individuo
    
