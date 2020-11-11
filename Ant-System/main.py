from utils import *
from constants import *
from AntSystem import *

dist = readDistFile('LAU15.txt')

ant_system = AntSystem(dist, ITERATIONS, ALPHA, BETA, EVAPORATION_RATE, Q)
ant_system.initPheromone()
ant_system.initAnts()

for t in range(ant_system.iterations):
    for ant in ant_system.population:
        while (len(ant.solution) < ant_system.node_count):
            ant_system.goToNextNode(ant)
        ant.evaluation = ant_system.calculateFO(ant.solution)
        if (ant.evaluation < ant_system.best_evaluation):
            print(f'Iteração: {t}\t->\tSolução: {ant.solution}\tAvaliação: {ant.evaluation}')
            ant_system.best_solution = ant.solution
            ant_system.best_evaluation = ant.evaluation
    ant_system.pheromoneUpdate()
    ant_system.restartAnts()


    
