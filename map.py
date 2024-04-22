
class Map:
    def __init__(self):
        self.cities = {}
        self.roads = {}

    def add_city(self, city):
        self.cities[city.name] = city