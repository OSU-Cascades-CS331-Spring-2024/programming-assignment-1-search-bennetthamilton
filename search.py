# Description: Search algorithm classes to represent each algorithm (breadth-first search, 
#              iterative deepening depth-limited search, uniform-cost search, and A* search)

# ref: https://docs.python.org/3/library/queue.html
import sys
import queue
import json

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
        self.parents = {}
        self.path = []
        self.frontier = []          # the queue of nodes to be expanded
        self.explored = set()       # the set of nodes that have been expanded
        self.nodes_explored = 0     # the number of nodes removed from the frontier
        self.nodes_expanded = 0     # the total number of successors
        self.nodes_maintained = 0   # the number of nodes stored in the frontier

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
    
    def search(self):
        raise NotImplementedError
    
    def get_path(self):
        return self.path
    
    def construct_path(self):
        current = self.end_city
        while current is not None:
            self.path.append(current)
            current = self.parents[current]
        self.path.reverse()

    def get_results(self):
        self.construct_path()
        result_dict = {
            "algorithm": self.__class__.__name__,
            "initial_city": self.start_city,
            "goal_city": self.end_city,
            "path": self.path,
            "cost": self.map_data.compute_path_distance(self.path),
            "nodes_explored": self.nodes_explored,
            "nodes_expanded": self.nodes_expanded,
            "nodes_maintained": self.nodes_maintained
        }
        # convert results to string from dict
        # ref: https://docs.python.org/3/library/json.html
        results = json.dumps(result_dict, indent=4)
        return results
        
    
# Subclasses: BFS, IDS, UCS, A*
class BreadthFirstSearch(SearchAlgorithm):

    # ref: https://www.geeksforgeeks.org/python-program-for-breadth-first-search-or-bfs-for-a-graph/
    def search(self):
        q = queue.Queue()
        q.put(self.start_city)
        self.explored.add(self.start_city)
        self.parents = {self.start_city: None}
        
        while not q.empty():
            current_city = q.get()
            
            if current_city == self.end_city:
                break
            
            for city in self.map_data.connections[current_city]:
                if city not in self.explored:
                    q.put(city)
                    # update metrics
                    self.explored.add(city)
                    self.nodes_explored += 1
                    self.nodes_expanded += 1
                    self.nodes_maintained = q.qsize()
                    self.parents[city] = current_city

        # print success message
        print("Success! Path found from {} to {} for bfs.".format(self.start_city, self.end_city))

class IterativeDLS(SearchAlgorithm):
    def __init__(self, map_data, start_city, end_city, depth_limit=sys.maxsize):
        super().__init__(map_data, start_city, end_city)
        self.depth_limit = depth_limit

    def search(self):
        # ref: https://www.geeksforgeeks.org/iterative-deepening-searchids-iterative-deepening-depth-first-searchiddfs/
        def recursive_dls(city, depth):
            if depth == 0:
                return False
            if city == self.end_city:
                return True
            if depth > 0:
                for connected_city in self.map_data.connections[city]:
                    if recursive_dls(connected_city, depth-1):
                        # update metrics
                        self.nodes_explored += 1
                        self.frontier.append(connected_city)
                        self.explored.add(connected_city)
                        self.parents[connected_city] = city
                        return True
        
        for depth in range(self.depth_limit):
            if recursive_dls(self.start_city, depth):
                # print success message
                print("Success! Path found from {} to {} for dls.".format(self.start_city, self.end_city))
                return True

        return False

class UniformCostSearch(SearchAlgorithm):
    def search(self):
        pq = queue.PriorityQueue()
        pq.put((0, self.start_city))
        self.frontier.append(self.start_city)
        self.explored.add(self.start_city)
        cost_so_far = {self.start_city: 0}

        while not pq.empty():
            current_cost, current_city = pq.get()
            
            if current_city == self.end_city:
                break
            
            for city in self.map_data.connections[current_city]:
                new_cost = current_cost + self.map_data.get_distance(current_city, city)
                if city not in cost_so_far or new_cost < cost_so_far[city]:
                    cost_so_far[city] = new_cost
                    pq.put((new_cost, city))
                    self.frontier.append(city)
                    self.explored.add(city)
                    self.parents[city] = current_city

            # update metrics
            self.nodes_explored += 1
            self.nodes_maintained = pq.qsize()

        # print success message
        print("Success! Path found from {} to {} for ucs.".format(self.start_city, self.end_city))


class AStarSearch(SearchAlgorithm):
    def search(self):
        pq = queue.PriorityQueue()
        pq.put((0 + self.heuristic(self.start_city), self.start_city))
        self.frontier.append(self.start_city)
        self.explored.add(self.start_city)
        cost_so_far = {self.start_city: 0}

        while not pq.empty():
            current_cost, current_city = pq.get()
            
            if current_city == self.end_city:
                break
            
            for city in self.map_data.connections[current_city]:
                new_cost = cost_so_far[current_city] + self.map_data.get_distance(current_city, city)
                if city not in cost_so_far or new_cost < cost_so_far[city]:
                    cost_so_far[city] = new_cost
                    pq.put((new_cost + self.heuristic(city), city))
                    self.frontier.append(city)
                    self.explored.add(city)
                    self.parents[city] = current_city

            # update metrics
            self.nodes_explored += 1
            self.nodes_maintained = pq.qsize()

        # print success message
        print("Success! Path found from {} to {} for astar.".format(self.start_city, self.end_city))

    def heuristic(self, city):
        return self.map_data.get_coordinate_distance(city, self.end_city)
