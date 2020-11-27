import os
import shutil
import time
import numpy as np
from constants import *
from PSO import *
import matplotlib.pyplot as plt

# parameters
iterations_list = [50, 100, 150]
swarm_list = [25, 50, 100]
c1_list = [0.5, 1.5, 2.5]
c2_list = [0.5, 1.5, 2.5]
w_list = [0.25, 0.5, 0.75, 1]

# constants
number_of_executions = 20
filesFolderName = 'files'
graphFolderName = 'graphs'

def fileOperations(best, worst, average, iterations, c1, c2, w, count):

    path = f'{filesFolderName}/{iterations}-{c1}-{c2}-{w}'
    with open(f'{path}/{count}.txt', "a") as f:
        f.write(f'{best} {worst} {average}\n')

    
def createFolders():

    if os.path.exists(filesFolderName):
        shutil.rmtree(filesFolderName)
    os.makedirs(filesFolderName)
    
    for iterations in iterations_list:
        for c1 in c1_list:
            for c2 in c2_list:
                for w in w_list:   
                    path = f'{filesFolderName}/{iterations}-{c1}-{c2}-{w}'
                    os.makedirs(path)

    if not os.path.exists(graphFolderName):  
        os.makedirs(graphFolderName)


def runPSO(iterations, c1, c2, w, execution):
    
    pso = PSO(SWARM_SIZE, iterations, w, c1, c2)
    pso.generateSwarm()

    for iteration in range(pso.iterations):
        for idx, particle in enumerate(pso.swarm):
            pso.calculateFitness(particle)
            if (particle.fitness < particle.pbest[FITNESS]):
                particle.pbest = [particle.fitness, particle.x]
            pso.setNeighborGBest(particle, idx)
            particle.v = pso.updateParticleVelocity(particle)
            particle.x = pso.updateParticleSolution(particle)
        (best, worst, average) = pso.getMetricsOfIteration()
        fileOperations(best, worst, average, iterations, c1, c2, w, execution)


    # best_solution = pso.getBestSolution()
    # print(f'\nBest solution\t->\tFitness: {best_solution.pbest[FITNESS]}\tSolution: {best_solution.pbest[SOLUTION]}')



def runToAllCombinations():
    for iterations in iterations_list:
        for c1 in c1_list:
            for c2 in c2_list:
                for w in w_list:
                    print(f'{iterations}-{c1}-{c2}-{w}')
                    for execution in range(number_of_executions):
                        runPSO(iterations, c1, c2, w, execution)


def readFilesAndGenerateGraphs():

    average_fitness = []
    for iterations in iterations_list:
        for c1 in c1_list:
            for c2 in c2_list:
                for w in w_list:

                    filesData = []
                    folder = f'{iterations}-{c1}-{c2}-{w}' 
                    print(f'{folder}')
                
                    for filename in os.listdir(f'{os.getcwd()}/{filesFolderName}/{folder}'):
                        with open(os.path.join(f'{os.getcwd()}/{filesFolderName}/{folder}', filename), 'r') as f:
                            arrayLines = []
                            for lines in f:
                                lines = lines.split(' ')
                                lines[2] = lines[2][:-2]
                                arrayLines.append(lines)

                        filesData.append(arrayLines)

                    data_array = np.zeros((len(filesData[0]), len(filesData[0][0])))

                    summation = 0
                    for iteration in range(len(filesData[0])):
                        for data in range(len(filesData[0][0])):
                            for file in range(len(filesData)):   # para cada uma das n execucoes
                                summation += float(filesData[file][iteration][data])
                            data_array[iteration][data] = summation/len(filesData)
                            summation = 0
                    
                    summation_best_fitness = 0
                    for file in filesData:
                        fitness = []
                        for iteration in file:
                            fitness.append(abs(float(iteration[0])))
                        val, idx = min((val, idx) for (idx, val) in enumerate(fitness))
                        summation_best_fitness += val
                    average_fitness.append([folder, summation_best_fitness/len(filesData)])   

                    # PLOTA E SALVA OS GRAFICOS
                    plt.rcParams.update({'figure.max_open_warning': 0})
                    fig = plt.figure(figsize=(8, 4))
                    fig.suptitle(folder)
                    plt.axhline(y=0, linewidth=0.5, color='r', linestyle='--')
                    plt.xlabel('Iteration')
                    plt.ylabel('Fitness')
                    plt.plot(data_array)
                    plt.legend(['Best Solution', 'Best Particle', 'Worst Particle', 'Average Particle'], loc='upper right', fontsize='xx-small')
                    fig.savefig(f'{graphFolderName}/{folder}.png', dpi=fig.dpi)

    average_fitness = sorted(average_fitness, key=lambda x: x[1])
    with open(f'{filesFolderName}/fitness.txt', 'w') as f:
        for item in average_fitness:
            f.write(f'{item[0]}\t\t{item[1]}\n')

start = time.time()
# print("Creating directories...")
# createFolders()
# print("Running algorithm...")
# runToAllCombinations()
print("Reading output files and generating graphs...")
readFilesAndGenerateGraphs()
end = time.time()
print(f'\nTime elapsed: {end - start} seconds')