# ESTE ARQUIVO É IGUAL AO main.py 
# PORÉM ELE EXECUTA O CODIGO 20X PARA CADA DAS 81 CONFIGURAÇÕES DE PARAMETROS POSSIVEIS
# RESULTANDO NUM TOTAL DE 1620 EXECUÇÕES

from utils import fileOperations
from AG import *
from params import *

def runToAllCombination():

    for mutacao in mutacaoArray:
        for cruzamento in cruzamentoArray:
            for populacao in populacaoArray:
                for geracoes in geracoesArray:
                    for execution in range(20):
        
                    # AG(tamanho da populacao, numero de geracoes, taxa de mutacao, taxa de cruzamento, numero de genes, xmin, xmax, alpha, beta)
                        ag  = AG(int(populacao), int(geracoes), int(mutacao), int(cruzamento), 2, -2, 2, 0.75, 0.25)
                        populacao_inicial = ag.geraPopulacao()
                        populacao_atual = ag.defineIndividuos(populacao_inicial)

                        for geracao in range(ag.num_geracoes):

                            ag.fitPopulacao(populacao_atual)
                            melhorIndividuo = (ag.getMelhorIndividuo(populacao_atual))
                            piorIndividuo = (ag.getPiorIndividuo(populacao_atual))
                            mediaIndividuos = (ag.getMediaIndividuos(populacao_atual))

                            pais = ag.roleta(populacao_atual)

                            populacao_atual = []
                            filhos = ag.crossover(pais, 'alphabeta')
                            populacao_atual = filhos

                            ag.mutacao(populacao_atual)
                            populacao_atual.pop(randint(0, len(populacao_atual)-1))
                            populacao_atual.append(melhorIndividuo)

                            fileOperations(melhorIndividuo, piorIndividuo, mediaIndividuos, filesFolderName, ag.taxa_mutacao, ag.taxa_cruzamento, ag.tam_populacao, ag.num_geracoes, execution)