from sys import argv
import matplotlib.pyplot as plt
import numpy as np
import os

from params import *

def createGraphs():

  if not os.path.exists(graphFolderName):
    os.makedirs(graphFolderName)

  cont = 1

  # LE OS ARQUIVOS, AGRUPA OS DADOS E TIRA AS MEDIAS
  for mutacao in mutacaoArray:
      for cruzamento in cruzamentoArray:
          for populacao in populacaoArray:
              for geracoes in geracoesArray:

                filesData = []
                
                folder = f'{mutacao}-{cruzamento}-{populacao}-{geracoes}' 

                for filename in os.listdir(f'{os.getcwd()}/files/{folder}'):
                  with open(os.path.join(f'{os.getcwd()}/files/{folder}', filename), 'r') as f:
                    arrayLines = []
                    for lines in f:
                      lines = lines.split(' ')
                      lines[2] = lines[2][:-2]
                      arrayLines.append(lines)

                  filesData.append(arrayLines)

                sumArray = np.zeros((len(filesData[0]), len(filesData[0][0])))
                soma = 0

                for geracao in range(len(filesData[0])):
                  for data in range(len(filesData[0][0])):
                    for file in range(len(filesData)):   # para cada uma das n execucoes
                      soma += float(filesData[file][geracao][data])
                    sumArray[geracao][data] = soma/len(filesData)
                    soma = 0
                  

                # PLOTA E SALVA OS GRAFICOS
                plt.rcParams.update({'figure.max_open_warning': 0})
                fig = plt.figure(figsize=(6, 3.2))
                fig.suptitle(folder)
                plt.yticks(np.arange(0, 10, 0.75))
                plt.plot(sumArray)
                plt.legend(['Melhor Indivíduo', 'Pior Indivíduo', 'Média dos Indivíduos'], loc='upper right', fontsize='xx-small')
                # plt.show()
                fig.savefig(f'{graphFolderName}/{folder}.png', dpi=fig.dpi)
                cont += 1   