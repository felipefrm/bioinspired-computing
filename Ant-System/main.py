from utils import *
from constants import *
from AntSystem import *

dist = readDistFile('LAU15.txt')

ant_system = AntSystem(dist, len(dist) * POP_MULTIPLIER, ITERATIONS, ALPHA, BETA, EVAPORATION_RATE, Q)
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
            print(f'Iteration: {t}\tSolution: {ant.solution}\tEvaluation: {ant.evaluation}')
            ant_system.best_solution = ant.solution
            ant_system.best_evaluation = ant.evaluation
    
    print(f'Best evaluation of iteration {t}: {best_evaluation_iter}')

    ant_system.pheromoneUpdate()
    ant_system.restartAnts()


    
