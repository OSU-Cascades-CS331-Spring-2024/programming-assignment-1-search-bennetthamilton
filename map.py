# Descriptions: Map class to represent a map of cities (obj) and connections (dict)
import math

class Map:
    def __init__(self):
        self.cities = {}
        self.connections = {}

    def add_city(self, city):
        self.cities[city.name] = city

    def add_connection(self, city1, city2, distance):
        if city1 not in self.connections:
            self.connections[city1] = {}
        self.connections[city1][city2] = distance

    def get_distance(self, city1, city2):
        return self.connections[city1][city2]
    
    def compute_path_distance(self, path):
        total_distance = 0
        for i in range(len(path) - 1):
            total_distance += self.get_distance(path[i], path[i+1])
        return total_distance
    
    def get_coordinate_distance(self, city1, city2):
        lat1, long1 = self.cities[city1].coordinates
        lat2, long2 = self.cities[city2].coordinates
        distance = math.sqrt((lat2 - lat1)**2 + (long2 - long1)**2)