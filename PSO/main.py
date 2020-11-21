from PSO import *
from constants import *
from func_obj import func_obj

pso = PSO(SWARM_SIZE, W, C1, C2)
pso.generateSwarm()
pso.setTopology()
for iteration in range(ITERATIONS):
    for particle in pso.swarm:
        pso.calculateFitness(particle)
        if (particle.fitness < particle.pbest[FITNESS]):
            particle.pbest = [particle.fitness, particle.x]
            if particle.fitness == particle.gbest[FITNESS]:
                particle.gbest == [particle.fitness, particle.x]
        pso.updateParticleVelocity(particle)
        pso.updateParticleSolution(particle)

for particle in pso.swarm:
    print(particle.gbest)