import os
import shutil
from constants import *
from utils import *
from AntSystem import *
import matplotlib.pyplot as plt

# parameters
iterations_list = [25, 50, 100]
alpha_list = [0, 1, 2]
beta_list = [0, 3, 5]
evaporation_list = [0.25, 0.5, 0.75]

# constants
number_of_executions = 20
instance = 'LAU15.txt'
filesFolderName = 'files'
graphFolderName = 'graphs'
optimalFolderName = 'optimal'

def fileOperations(best, iterations, alpha, beta, evaporation_rate, count, endAlgorithm):

    path = f'{filesFolderName}/{iterations}-{alpha}-{beta}-{evaporation_rate}'
    optimal = f'{filesFolderName}/{optimalFolderName}/{iterations}-{alpha}-{beta}-{evaporation_rate}'
    if not endAlgorithm:
        with open(f'{path}/{count}.txt', "a") as f:
            f.write(f'{best}\n')

    if endAlgorithm:
        with open(f'{optimal}.txt', "a") as f:
            f.write(f'{1 if best == 291 else 0}')
        
    
def createFolders():

    if os.path.exists(filesFolderName):
        shutil.rmtree(filesFolderName)
    os.makedirs(filesFolderName)
    
    for iterations in iterations_list:
        for alpha in alpha_list:
            for beta in beta_list:
                for evaporation_rate in evaporation_list:
                    
                    path = f'{filesFolderName}/{iterations}-{alpha}-{beta}-{evaporation_rate}'
                    os.makedirs(path)
                    optimal = f'{filesFolderName}/{optimalFolderName}'
                    os.makedirs(optimal, exist_ok=True)


    if not os.path.exists(graphFolderName):  
        os.makedirs(graphFolderName)


def runAntSystem(iterations, alpha, beta, evaporation_rate, execution):
    
    dist = readDistFile(instance)

    ant_system = AntSystem(dist, iterations, alpha, beta, evaporation_rate, Q)
    ant_system.initPheromone()
    ant_system.initAnts()

    for t in range(ant_system.iterations):
        best_evaluation_iter = float('inf') 
        for ant in ant_system.population:
            while (len(ant.solution) < ant_system.node_count):
                ant_system.goToNextNode(ant)
            ant.solution.append(ant.solution[0])
            ant.evaluation = ant_system.calculateFO(ant.solution)

            if (ant.evaluation < best_evaluation_iter):
                best_evaluation_iter = ant.evaluation

            if (ant.evaluation < ant_system.best_evaluation):
                ant_system.best_solution = ant.solution
                ant_system.best_evaluation = ant.evaluation
        
        fileOperations(best_evaluation_iter, iterations, alpha, beta, evaporation_rate, execution, 0)

        ant_system.pheromoneUpdate()
        ant_system.restartAnts()

    fileOperations(ant_system.best_evaluation, iterations, alpha, beta, evaporation_rate, execution, 1)

def runToAllCombinations():
    for iterations in iterations_list:
        for alpha in alpha_list:
            for beta in beta_list:
                for evaporation_rate in evaporation_list:
                    print(f'{iterations}-{alpha}-{beta}-{evaporation_rate}')
                    for execution in range(number_of_executions):
                        runAntSystem(iterations, alpha, beta, evaporation_rate, execution)


def readFilesAndGenerateGraphs():

    optimal_data = []
    x_axis = []
    for filename in os.listdir(f'{os.getcwd()}/{filesFolderName}/{optimalFolderName}'):
        with open(os.path.join(f'{os.getcwd()}/{filesFolderName}/{optimalFolderName}', filename), 'r') as f:
            read_file = f.read()
            optimal_data.append(read_file.count('1'))
            x_axis.append(filename[:-4])

    for iterations in iterations_list:
        for alpha in alpha_list:
            for beta in beta_list:
                for evaporation_rate in evaporation_list:

                    print(f'{iterations}-{alpha}-{beta}-{evaporation_rate}')
                  
                    files_data = []                    
                    folder = f'{iterations}-{alpha}-{beta}-{evaporation_rate}'
                    for filename in os.listdir(f'{os.getcwd()}/{filesFolderName}/{folder}'):
                        with open(os.path.join(f'{os.getcwd()}/{filesFolderName}/{folder}', filename), 'r') as f:
                            arrayLines = []
                            for lines in f:
                                arrayLines.append(lines[:-1])
                        files_data.append(arrayLines)
                    
                    data = []
                    add = 0
                    for i in range(len(files_data[0])):
                        for file in range(len(files_data)):
                            add += int(files_data[file][i])
                        data.append(add/len(files_data))
                        add = 0

                    plt.rcParams.update({'figure.max_open_warning': 0})
                    fig = plt.figure(figsize=(6, 4))
                    fig.suptitle(folder)
                    plt.axhline(y=291, linewidth=0.5, color='r', linestyle='--')
                    plt.text(0,291, "{:.0f}".format(291), color="red", ha="center", va="center")
                    plt.xlabel('iteration')
                    plt.ylabel('evaluation')
                    plt.plot(data)
                    plt.legend(['Optimal solution', 'Best individual'], loc='upper right', fontsize='xx-small')
                    fig.savefig(f'{graphFolderName}/{folder}.png', dpi=fig.dpi)

    colors = []
    for value in optimal_data:
        if value == number_of_executions:
            colors.append('blue')
        else:
            colors.append('red')
  
    print(len(optimal_data))
    print(len(x_axis))

    y_pos = np.arange(len(x_axis))
    fig = plt.figure(figsize=(40,20))
    plt.bar(y_pos, optimal_data, align='center', color=colors)
    plt.xticks(y_pos, x_axis, rotation=90, fontsize=14)
    plt.ylabel('how many times was found the optimal solution', fontsize=18)
    plt.title('Optimal x Combination', fontsize=24)
    fig.savefig(f'{graphFolderName}/{optimalFolderName}.png', dpi=fig.dpi) 


print("Creating directories...")
createFolders()
print("Running algorithm...")
runToAllCombinations()
print("Reading output files and generating graphs...")
readFilesAndGenerateGraphs()