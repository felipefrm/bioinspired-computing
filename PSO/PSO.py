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

    def setNeighborGBest(self, particle, idx):
        neighbors_index = [(idx-1)%self.swarm_size, (idx+1)%self.swarm_size]
        neighbors1 = self.swarm[neighbors_index[0]].pbest
        neighbors2 = self.swarm[neighbors_index[1]].pbest
        # print(particle.pbest[FITNESS], neighbors1[FITNESS], neighbors2[FITNESS])
        if neighbors1[FITNESS] < neighbors2[FITNESS] and neighbors1[FITNESS] < particle.pbest[FITNESS]:
            particle.gbest = [neighbors1[FITNESS], neighbors1[SOLUTION]]
        elif neighbors2[FITNESS] < neighbors1[FITNESS] and neighbors2[FITNESS] < particle.pbest[FITNESS]:
            particle.gbest = [neighbors2[FITNESS], neighbors2[SOLUTION]]
        else:
            particle.gbest = [particle.pbest[FITNESS], particle.pbest[SOLUTION]]
        # print(particle.gbest)
        # exit()

    def calculateFitness(self, particle):
        particle.fitness = func_obj(particle.x)

    def updateParticleVelocity(self, particle):
        new_velocity = []
        for j in range(len(particle.x)):
            r1 = random()
            r2 = random()
            pbest = self.c1*r1 * (particle.pbest[SOLUTION][j] - particle.x[j])
            gbest = self.c2*r2 * (particle.gbest[SOLUTION][j] - particle.x[j])
            v = self.w*particle.v[j] + pbest + gbest
            new_velocity.append(v)
        return new_velocity

    def updateParticleSolution(self, particle):
        new_solution = [x + y for x, y in zip(particle.x, particle.v)]
        limits = [[X1MIN, X1MAX], [X2MIN, X2MAX], [X3MIN, X3MAX]]
        for i in range(len(particle.x)):
            if new_solution[i] < limits[i][0]:
                new_solution[i] = limits[i][0]
            elif new_solution[i] > limits[i][1]:
                new_solution[i] = limits[i][1]
        return new_solution

    def getBestSolution(self):
        fitness = []
        for idx, particle in enumerate(self.swarm):
            print(f'Particle {idx}\t->\tFitness: {particle.pbest[FITNESS]}\tSolution: {particle.pbest[SOLUTION]}')
            fitness.append(abs(particle.pbest[FITNESS]))

        val, idx = min((val, idx) for (idx, val) in enumerate(fitness))

        return self.swarm[idx]