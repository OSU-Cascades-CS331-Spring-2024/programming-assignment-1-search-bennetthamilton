# Description: Search algorithm classes to represent each algorithm (breadth-first search, 
#              iterative deepening depth-limited search, uniform-cost search, and A* search)

from collections import deque

class SearchAlgorithm:
    # ref: https://www.digitalocean.com/community/tutorials/python-static-method
    @staticmethod
    def from_name(name, map_data, start_city, end_city):
        if name == "bfs":
            return BreadthFirstSearch(map_data, start_city, end_city)
        elif name == "dls":
            return IterativeDLS(map_data, start_city, end_city)
        elif name == "ucs":
            return UniformCostSearch(map_data, start_city, end_city)
        elif name == "astar":
            return AStarSearch(map_data, start_city, end_city)
        else:
            raise ValueError("Unknown search algorithm: {}".format(name))
        
    def __init__(self, map_data, start_city, end_city):
        self.map_data = map_data
        self.start_city = start_city
        self.end_city = end_city

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