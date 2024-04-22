# Title: Programming Assignment 1 – Search
# Name: Bennett Hamilton
# Collaborators: Ashley Doerfler
# Date: 4/22/2024
# Description: This program reads a map file (ex. france.txt) and uses 
#              a search algorithm to find the shortest path from the start 
#              to the goal. The program will output the path and the cost
#              of the path(s) in a solutions.txt file.

import sys
import argparse
from map import Map
from city import City
from search import SearchAlgorithm

# define constants
SEARCH_ALGOS = ["bfs", "dls", "ucs", "astar"]

# function to parse command line arguments
# ref: https://docs.python.org/3/library/argparse.html
def parse_args():
    # check for correct number of arguments
    if len(sys.argv) < 2:
        print("Usage: python script.py <map_file> [-A START_CITY] [-B END_CITY] [-S SEARCH_ALGORITHM]")
        sys.exit(1)
    
    # get command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("map_file", help="Text file containing map data")
    parser.add_argument("-A", "--start_city", help="Starting city")
    parser.add_argument("-B", "--end_city", help="Ending city")
    parser.add_argument("-S", "--search_algorithm", choices=SEARCH_ALGOS, default=SEARCH_ALGOS[0], help="Search algorithm to use (default: BFS)")

    print("Parsing command line arguments...")

    return parser.parse_args()

# function to read map data from file
def read_map_data(map_file):
    map_data = Map()

    print("Reading map data from file...")

    with open(map_file, "r") as file:
        # read each line in file
        for line in file:
            # split into city and edges
            parts = line.strip().split(" --> ")
            city_info = parts[0].split()
            edges = parts[1].split()

            # assign city data
            city_name = city_info[0]
            latitude = float(city_info[1]) + float(city_info[2])/60 + float(city_info[3])/3600
            longitude = float(city_info[5]) + float(city_info[6])/60 + float(city_info[7])/3600
            coordinate = (latitude, longitude)

            # add city to map
            map_data.add_city(City(city_name, coordinate))

            # assign edge data
            edges = parts[1].split()
            for i in range(0, len(edges), 2):
                connected_city = edges[i][3:]   # remove 'va-' from city name
                distance = float(edges[i+1])
                map_data.add_connection(city_name, connected_city, distance)

    print("Map data read successfully!")
            
    return map_data

# function to run search algorithm
def run_search(map, start_city, end_city, search_algorithm):
    # create search algorithm object
    pass

# function to run all search algorithms
def run_all_searches(map, start_city, end_city):
    for algorithm in SEARCH_ALGOS:
        run_search(map, start_city, end_city, algorithm)

# main function to run program
def main():
    # Parse command line arguments
    args = parse_args()
    map_file = args.map_file

    # Read map data from file
    map_data = read_map_data(map_file)

    # if start and end are not provided, use predefined city pairs
    if not (args.start and args.goal):
        city_pairs = [
            ("Brest", "Nice"),
            ("Montpellier", "Calais"),
            ("Strasbourg", "Bordeaux"),
            ("Paris", "Grenoble"),
            ("Grenoble", "Paris"),
            ("Brest", "Grenoble"),
            ("Grenoble", "Brest"),
            ("Nice", "Nantes"),
            ("Caen", "Strasbourg")
        ]
        for start, goal in city_pairs:
            # Perform search for given city pairs using all search algorithm
            run_all_searches(map_data, start, goal)
            # Write results to solutions.txt
        pass
    else:
        # Perform search for given start and goal cities using specified search algorithm
        run_search(map_data, args.start_city, args.end_city, args.search_algorithm)
        # Write results to solutions.txt
        pass

if __name__ == "__main__":
    main()