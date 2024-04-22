# Description: Search algorithm classes to represent each algorithm (breadth-first search, 
#              iterative deepening depth-limited search, uniform-cost search, and A* search)

from collections import deque

class SearchAlgorithm:
    def __init__(self, problem):
        self.problem = problem

    def search(self):
        raise NotImplementedError
    
# Subclasses: BFS, IDS, UCS, A*
class BreadthFirstSearch(SearchAlgorithm):
    def search(self):
        # todo: implement breadth-first search
        pass

class IterativeDLS(SearchAlgorithm):
    def search(self):
        # todo: implement iterative depth-limited search
        pass

class UniformCostSearch(SearchAlgorithm):
    def search(self):
        # todo: implement uniform-cost search
        pass

class AStarSearch(SearchAlgorithm):
    def search(self):
        # todo: implement A* search
        pass