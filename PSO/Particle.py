from func_obj import func_obj

class Particle():

    def __init__(self, x):
        self.x = x
        self.v = [0 for i in range(len(x))]
        self.fitness = None
        self.pbest = [self.fitness, self.x]
        self.gbest = []