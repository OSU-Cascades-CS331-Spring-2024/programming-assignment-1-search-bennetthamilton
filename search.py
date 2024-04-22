
class SearchAlgorithm:
    def __init__(self, problem):
        self.problem = problem

    def search(self):
        raise NotImplementedError
    
# Subclasses
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