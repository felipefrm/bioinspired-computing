class Ant():

    def __init__(self, start):
        self.solution = [start]
        self.evaluation = None
        self.start = start
        self.current = start
        # self.visited = [start]