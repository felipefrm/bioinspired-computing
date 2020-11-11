from utils import *
from random import uniform
import numpy as np
from constants import *

class Ant():

    def __init__(self, start):
        self.solution = [start]
        self.evaluation = None
        self.start = start
        self.current = start
        # self.visited = [start]

class AntSystem():

    def __init__(self, dist, iterations, alpha, beta, evaporation_rate, q):
        self.population_size = len(dist)# mesmas valores, mas por questão
        self.node_count = len(dist)    # de semantica no codigo, estão alocados 2 variaves 
        self.dist = dist
        self.iterations = iterations
        self.population = []
        self.pheromone = None
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.q = q 
        self.best_solution = None
        self.best_evaluation = float('inf')

    def initAnts(self):
        for i in range(self.population_size):
            self.population.append(Ant(i))

    def initPheromone(self):
        self.pheromone = np.full((self.population_size, self.population_size), 10 ** -16)
        for i in range(self.population_size):
            self.pheromone[i][i] = 0

    def calculateFO(self, solution):
        dist_sum = 0
        # solution = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        for i in range(len(solution)-1):
            print(f'foi de {solution[i]} para {solution[i + 1]} o que custou {self.dist[solution[i]][solution[i+1]]}')
            dist_sum += self.dist[solution[i]][solution[i+1]] 
        return dist_sum

    def goToNextNode(self, ant):
        not_visited = []
        prob_list = []
        divisor = 0
        for node in range(self.node_count):
            if node not in ant.solution:
                not_visited.append(node)
                divisor += ((self.pheromone[ant.current][node] ** self.alpha) * ((1/self.dist[ant.current][node]) ** self.beta)) 

       
        for node in not_visited:
            prob_list.append(((self.pheromone[ant.current][node] ** self.alpha) * ((1/self.dist[ant.current][node]) ** self.beta))/divisor)

        r = uniform(0, 1)
        acumulator = count = 0
        while (acumulator < r):
            acumulator += prob_list[count]
            count += 1
    
        ant.solution.append(not_visited[count-1])
        ant.current = not_visited[count-1] 

        return not_visited[count-1]

    def findEdgeInSolution(self, solution, edge):
        return any((solution[i], solution[i + 1]) == (edge[0], edge[1]) for i in range(len(solution) - 1))

    def pheromoneUpdate(self):
        for i in range(self.population_size):
            for j in range(self.population_size):
                sum_pheromone = 0
                for ant in self.population:
                    if (self.findEdgeInSolution(ant.solution, [i, j])):
                        sum_pheromone += self.q/ant.evaluation
                    else:
                        sum_pheromone += 0
                self.pheromone[i][j] = (1 - self.evaporation_rate) * self.pheromone[i][j] + sum_pheromone


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


    
