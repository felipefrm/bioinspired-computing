from sys import argv
import matplotlib.pyplot as plt
import numpy as np
import os


# LE OS ARQUIVOS, AGRUPA OS DADOS E TIRA AS MEDIAS
filesData = []

for filename in os.listdir(f'{os.getcwd()}/files/{argv[1]}'):
  with open(os.path.join(f'{os.getcwd()}/files/{argv[1]}', filename), 'r') as f:
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
  

# PLOTA O GRAFICO
fig = plt.figure(figsize=(6, 3.2))
plt.yticks(np.arange(0, 10, 0.75))
plt.plot(sumArray)
plt.legend(['Melhor Indivíduo', 'Pior Indivíduo', 'Média dos Indivíduos'], loc='upper right', fontsize='xx-small')
plt.show()