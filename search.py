# Description: Search algorithm classes to represent each algorithm (breadth-first search, 
#              iterative deepening depth-limited search, uniform-cost search, and A* search)

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
        self.path = []
        self.cost = 0
        self.frontier = []          # the queue of nodes to be expanded
        self.explored = set()       # the set of nodes that have been expanded
        self.nodes_explored = 0     # the number of nodes removed from the frontier
        self.nodes_expanded = 0     # the total number of successors
        self.nodes_maintained = 0   # the number of nodes stored in the frontier

    def search(self):
        raise NotImplementedError
    
# Subclasses: BFS, IDS, UCS, A*
class BreadthFirstSearch(SearchAlgorithm):
    # ref: https://www.geeksforgeeks.org/python-program-for-breadth-first-search-or-bfs-for-a-graph/
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