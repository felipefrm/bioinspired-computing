from random import uniform, sample
import numpy as np
from Ant import *

class AntSystem():

    def __init__(self, dist, pop_size, iterations, alpha, beta, evaporation_rate, q):
        self.population_size = round(pop_size)
        self.node_count = len(dist)     
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
        ratio = self.population_size/self.node_count
        if (ratio < 1):
            set_selected_nodes = sample(list(range(self.node_count)), self.population_size)
            for node in set_selected_nodes:
                self.population.append(Ant(node))
        else:
            if (ratio != int(ratio)):
                exit('If the population is bigger than the number of nodes, the population size must be divisible by the number of nodes.')
            for j in range(int(ratio)):
                for i in range(self.node_count):
                    self.population.append(Ant(i))

    def restartAnts(self):
        self.population = []
        self.initAnts()

    def initPheromone(self):
        self.pheromone = np.full((self.node_count, self.node_count), 10 ** -16)

    def calculateFO(self, solution):
        dist_sum = 0
        for i in range(len(solution)-1):
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
        for i in range(self.node_count):
            for j in range(self.node_count):
                sum_pheromone = 0
                for ant in self.population:
                    if (self.findEdgeInSolution(ant.solution, [i, j])):
                        sum_pheromone += self.q/ant.evaluation
                    else:
                        sum_pheromone += 0
                self.pheromone[i][j] = (1 - self.evaporation_rate) * self.pheromone[i][j] + sum_pheromone