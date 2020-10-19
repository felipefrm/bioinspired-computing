from time import time
import os

def fileOperations(melhorIndividuo, piorIndividuo, mediaIndividuos, folder, mutacao, cruzamento, populacao, geracoes, count):

  path = f'{folder}/{mutacao}-{cruzamento}-{populacao}-{geracoes}'

  with open(f'{path}/{count}.txt', "w") as f:
    for geracao in range(geracoes):
      f.write(f'{melhorIndividuo[geracao].fitness} {piorIndividuo[geracao].fitness} {mediaIndividuos[geracao]}\n')
