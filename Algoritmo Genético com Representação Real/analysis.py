from sys import argv
import matplotlib.pyplot as plt
import numpy as np
import os

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
  
plt.imshow(sumArray)
plt.show()