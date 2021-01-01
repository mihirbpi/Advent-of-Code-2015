from aocd import get_data
import re
import itertools

my_list = get_data(day=9, year=2015).split("\n")

parse_pattern = re.compile(r'(\w+) to (\w+) = (\w+)')
distances_dict = {}
cities = set()

for i in range(0, len(my_list)):
    string = my_list[i]
    matches = parse_pattern.finditer(string)
    match = list(matches)[0]
    start_city = match.group(1)
    end_city = match.group(2)
    distance = int(match.group(3))
    cities.add(start_city)
    cities.add(end_city)
    distances_dict[(start_city, end_city)] = distance
    distances_dict[(end_city, start_city)] = distance

routes = list(itertools.permutations(list(cities)))
possible_route_dists = set()

for route in routes:
    route_dist = 0

    for i in range(0, len(route) - 1):
        route_dist += distances_dict[(route[i], route[i+1])]

    possible_route_dists.add(route_dist)

print(max(possible_route_dists))
