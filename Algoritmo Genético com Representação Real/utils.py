from time import time
import os

def fileOperations(melhorIndividuo, piorIndividuo, mediaIndividuos, mutacao, cruzamento, populacao, geracoes):

  path = f'files/{mutacao}-{cruzamento}-{populacao}-{geracoes}'

  if not os.path.exists(path):
    os.makedirs(path)

  with open(f'{path}/{int(time())}.txt', "w") as f:
    for geracao in range(geracoes):
      f.write(f'{melhorIndividuo[geracao].fitness} {piorIndividuo[geracao].fitness} {mediaIndividuos[geracao]}\n')
