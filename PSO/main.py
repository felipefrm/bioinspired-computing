from PSO import *
from constants import *
import time

start = time.time()

pso = PSO(SWARM_SIZE, ITERATIONS, W, C1, C2)
pso.generateSwarm()

for iteration in range(pso.iterations):
    for idx, particle in enumerate(pso.swarm):
        pso.calculateFitness(particle)
        if (particle.fitness < particle.pbest[FITNESS]):
            particle.pbest = [particle.fitness, particle.x]
        pso.setNeighborGBest(particle, idx)
        particle.v = pso.updateParticleVelocity(particle)
        particle.x = pso.updateParticleSolution(particle)

best_solution = pso.getBestSolution()
print(f'\nBest solution\t->\tFitness: {best_solution.pbest[FITNESS]}\tSolution: {best_solution.pbest[SOLUTION]}')

end = time.time()
print(f'\nTime elapsed: {end - start} seconds')

