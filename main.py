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

# define constants
SEARCH_ALGORITHMS = ["bfs", "dls", "ucs", "astar"]

# function to parse command line arguments
# ref: https://docs.python.org/3/library/argparse.html
def parse_args():
    # check for correct number of arguments
    if len(sys.argv) < 2:
        print("Usage: python script.py <map_file> [-A START_CITY] [-B END_CITY]")
        sys.exit(1)
    
    # get command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("map_file", help="Text file containing map data")
    parser.add_argument("-A", "--start_city", help="Starting city")
    parser.add_argument("-B", "--end_city", help="Ending city")
    parser.add_argument("-S", "--search_algorithm", choices=SEARCH_ALGORITHMS, default=SEARCH_ALGORITHMS[0], help="Search algorithm to use (default: BFS)")

    return parser.parse_args()

# function to run search algorithm
def run_search(map_file, start_city, end_city, search_algorithm):
    # TODO
    pass

# function to run all search algorithms
def run_all_searches(map_file, start_city, end_city):
    for algorithm in SEARCH_ALGORITHMS:
        run_search(map_file, start_city, end_city, algorithm)

# main function to run program
def main():
    # Parse command line arguments
    args = parse_args()
    map_file = args.map_file

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
            run_all_searches(map_file, start, goal)
            # Write results to solutions.txt
        pass
    else:
        # Perform search for given start and goal cities using specified search algorithm
        run_search(map_file, args.start_city, args.end_city, args.search_algorithm)
        # Write results to solutions.txt
        pass

if __name__ == "__main__":
    main()