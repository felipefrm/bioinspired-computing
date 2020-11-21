import os
import shutil
import numpy as np
from sys import argv
import matplotlib.pyplot as plt
from utils import *
from AG import *
from Mochila import *


# variacoes de parametros para experimento fatorial completo
mutacaoArray = [1, 5, 10]
cruzamentoArray = [60, 80, 100]
populacaoArray = [25, 50, 100]
geracoesArray = [25, 50, 100]
elitismoArray = [True, False]
instanciaArray = ['01', '02', '03', '04', '05', '06', '07', '08']

filesFolderName = 'files'
graphFolderName = 'graphs'

def fileOperations(melhorIndividuo, piorIndividuo, mediaIndividuos, folder, instancia, elitismo, mutacao, cruzamento, populacao, geracoes, count):

    path = f'{folder}/{instancia}-{elitismo}-{mutacao}-{cruzamento}-{populacao}-{geracoes}'

    with open(f'{path}/{count}.txt', "a") as f:

        f.write(f'{melhorIndividuo.fitness} {piorIndividuo.fitness} {mediaIndividuos}\n')


def createFolders():
    # cria a pasta de arquivos
    if os.path.exists(filesFolderName):
        shutil.rmtree(filesFolderName)
    os.makedirs(filesFolderName)

    # cria a pasta de graficos
    if not os.path.exists(graphFolderName):  
        os.makedirs(graphFolderName)
        #dentro da past de graficos, cria uma pasta para cada instancia
        os.chdir(graphFolderName)
        for dir in instanciaArray:
            os.mkdir(dir)
        os.chdir('../')

def runToAllCombinations():

    createFolders()

    mediaFitness = []
    for instancia in instanciaArray:
        for elitismo in elitismoArray:
            for mutacao in mutacaoArray:
                for cruzamento in cruzamentoArray:
                    for populacao in populacaoArray:
                        for geracoes in geracoesArray:
                            print(f'{instancia}-{elitismo}-{mutacao}-{cruzamento}-{populacao}-{geracoes}')
                            path = f'{filesFolderName}/{instancia}-{elitismo}-{mutacao}-{cruzamento}-{populacao}-{geracoes}'
                            os.makedirs(path)
                            for execution in range(20):
                                (c, p, u, s) = leArquivos(instancia)
                                qtd_obj = quantidadeObjetos(p)
                                mochila = Mochila(qtd_obj, c, p, u, s)

                                # AG(tam da população, numero de geracões, taxa mutação, taxa_cruzamento, probabilidade de vitória, numero de bits por individuo, com ou sem elitismo)
                                ag  = AG(populacao, geracoes, mutacao, cruzamento, 90, qtd_obj, elitismo)
                                nova_populacao = ag.geraPopulacao()

                                for geracao in range(ag.num_geracoes):
                                    ag.avaliaPopulacao(nova_populacao, mochila)
                                    melhorIndividuo = ag.getMelhorIndividuo(nova_populacao)
                                    piorIndividuo = (ag.getPiorIndividuo(nova_populacao))
                                    mediaIndividuos = (ag.getMediaIndividuos(nova_populacao))

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
                                    
                                    fileOperations(melhorIndividuo, piorIndividuo, mediaIndividuos, filesFolderName, instancia, elitismo, ag.taxa_mutacao, ag.taxa_cruzamento, ag.tam_populacao, ag.num_geracoes, execution)


                            filesData = []

                            folder = f'{instancia}-{elitismo}-{mutacao}-{cruzamento}-{populacao}-{geracoes}' 
                        
                            for filename in os.listdir(f'{os.getcwd()}/{filesFolderName}/{folder}'):
                                with open(os.path.join(f'{os.getcwd()}/{filesFolderName}/{folder}', filename), 'r') as f:
                                    arrayLines = []
                                    for lines in f:
                                        lines = lines.split(' ')
                                        lines[2] = lines[2][:-2]
                                        arrayLines.append(lines)

                                filesData.append(arrayLines)

                            dados = np.zeros((len(filesData[0]), len(filesData[0][0])))

                            soma = 0
                            for geracao in range(len(filesData[0])):
                                for data in range(len(filesData[0][0])):
                                    for file in range(len(filesData)):   # para cada uma das n execucoes
                                        soma += float(filesData[file][geracao][data])
                                    dados[geracao][data] = soma/len(filesData)
                                    soma = 0
                            mediaFitness.append([folder, dados[len(filesData[0])-1][0]])    

                            if (instancia == '01'):
                                otimo = 309
                            elif (instancia == '02'):
                                otimo = 51
                            elif (instancia == '03'):
                                otimo = 150
                            elif (instancia == '04'):
                                otimo = 107
                            elif (instancia == '05'):
                                otimo = 900 
                            elif (instancia == '06'):
                                otimo = 1735
                            elif (instancia == '07'):
                                otimo = 1458
                            else:
                                otimo = 13549094    

                            # PLOTA E SALVA OS GRAFICOS
                            plt.rcParams.update({'figure.max_open_warning': 0})
                            fig = plt.figure(figsize=(8, 4))
                            fig.suptitle(folder)
                            plt.axhline(y=otimo, linewidth=0.5, color='r', linestyle='--')
                            plt.xlabel('gerações')
                            plt.ylabel('fitness')
                            plt.plot(dados)
                            plt.legend(['Solução Ótima', 'Melhor Indivíduo', 'Pior Indivíduo', 'Média dos Indivíduos'], loc='lower right', fontsize='xx-small')
                            fig.savefig(f'{graphFolderName}/{instancia}/{folder}.png', dpi=fig.dpi)

      
        mediaFitness = sorted(mediaFitness, key=lambda x: x[1])
        with open(f'{filesFolderName}/{instancia}fitness.txt', 'w') as f:
            for item in mediaFitness[::-1]:
                f.write(f'{item[0]}\t\t{item[1]}\n')
        mediaFitness = []

runToAllCombinations()