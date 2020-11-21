from random import uniform, random
from constants import *
from func_obj import func_obj
from Particle import Particle

class PSO():

    def __init__(self, swarm_size, w, c1, c2):
        self.swarm_size = swarm_size
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.swarm = []

    def generateSwarm(self):
        for i in range(self.swarm_size):
            x1 = uniform(X1MIN, X1MAX)
            x2 = uniform(X2MIN, X2MAX)
            x3 = uniform(X3MIN, X3MAX)
            self.swarm.append(Particle([x1, x2, x3]))

    def setTopology(self):
        for i, particle in enumerate(self.swarm):
            neighbors_index = [(i-1)%self.swarm_size, (i+1)%self.swarm_size]
            neighbors1 = self.swarm[neighbors_index[0]]
            neighbors2 = self.swarm[neighbors_index[1]]
            if neighbors1.fitness < neighbors2.fitness:
                particle.gbest = [neighbors1.fitness, neighbors1.x]
            else:
                particle.gbest = [neighbors2.fitness, neighbors2.x]

    def calculateFitness(self, particle):
        particle.fitness = func_obj(particle.x)

    def updateParticleVelocity(self, particle):
        for j in range(len(particle.x)):
            r1 = random()
            r2 = random()
            pbest = [self.c1*r1 * (x - particle.x[j]) for x in particle.pbest[SOLUTION]]
            gbest = [self.c2*r2 * (x - particle.x[j]) for x in particle.gbest[SOLUTION]]
            v = self.w*particle.v[j] + pbest + gbest
            particle.v[j] = v

    def updateParticleSolution(self, particle):
        particle.x = [x + y for x, y in zip(particle.x, particle.v)]
        limits = [[X1MIN, X1MAX], [X2MIN, X2MAX], [X3MIN, X3MAX]]
        for i in range(len(particle.x)):
            if particle.x[i] < limits[i][0]:
                particle.x[i] = limits[i][0]
            elif particle.x[i] > limits[i][1]:
                particle.x[i] = limits[i][1]
