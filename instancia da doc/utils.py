from time import time
import os

def fileOperations(melhorIndividuo, piorIndividuo, mediaIndividuos, folder, mutacao, cruzamento, populacao, geracoes, count):

  path = f'{folder}/{mutacao}-{cruzamento}-{populacao}-{geracoes}'

  with open(f'{path}/{count}.txt', "a") as f:

    f.write(f'{melhorIndividuo.fitness} {piorIndividuo.fitness} {mediaIndividuos}\n')
