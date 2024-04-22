# Descriptions: Map class to represent a map of cities (obj) and connections (dict)
class Map:
    def __init__(self):
        self.cities = {}
        self.connections = {}

    def add_city(self, city):
        self.cities[city.name] = city

    def add_connection(self, city1, city2, distance):
        if city1 not in self.roads:
            self.roads[city1] = {}
        self.roads[city1][city2] = distance