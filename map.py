
class Map:
    def __init__(self):
        self.cities = {}
        self.roads = {}

    def add_city(self, city_name, coordinates):
        """
        add city to map

        params:
            city_name (str): name of city
            coordinates (tuple): coordinates of city

        return none
        """
        self.cities[city_name] = coordinates

    def add_road(self, city1, city2, distance):
        """
        add road to map

        params:
            city1 (str): name of city 1
            city2 (str): name of city 2
            distance (int): distance between city 1 and city 2

        return none
        """
        if city1 not in self.roads:
            self.roads[city1] = {}
        self.roads[city1][city2] = distance

        if city2 not in self.roads:
            self.roads[city2] = {}
        self.roads[city2][city1] = distance