from utils import *
from constants import *
from AntSystem import *

dist = readDistFile('LAU15.txt')

ant_system = AntSystem(dist, POP_SIZE, ALPHA, BETA, EVAPORATION_RATE, Q)
ant_system.initAnts()
ant_system.initPheromone()

for t in range(ant_system.iterations):
    for ant in ant_system.population:
        while (len(ant.solution) < ant_system.node_count):
            print(ant.solution)
            ant_system.goToNextNode(ant)
        ant.evaluation = ant_system.calculateFO(ant.solution)
        if (ant.evaluation < ant_system.best_evaluation):
            ant_system.best_solution = ant.solution
            ant_system.best_evaluation = ant.evaluation
    ant_system.pheromoneUpdate()

print(ant_system.best_solution)
print(ant_system.best_evaluation)


    
