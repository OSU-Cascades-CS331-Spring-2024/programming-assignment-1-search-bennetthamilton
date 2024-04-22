# Description: Search algorithm classes to represent each algorithm (breadth-first search, 
#              iterative deepening depth-limited search, uniform-cost search, and A* search)
class SearchAlgorithm:
    def __init__(self, problem):
        self.problem = problem

    def search(self):
        raise NotImplementedError
    
# Subclasses: BFS, IDS, UCS, A*
class BreadthFirstSearch(SearchAlgorithm):
    def search(self):
        pass

class IterativeDLS(SearchAlgorithm):
    def search(self):
        pass

class UniformCostSearch(SearchAlgorithm):
    def search(self):
        pass

class AStarSearch(SearchAlgorithm):
    def search(self):
        pass