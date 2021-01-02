from aocd import get_data
import re
import itertools
import math

my_list = get_data(day=15, year=2015).split("\n")
parse_pattern = re.compile(r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)')
ingredient_info_dict = {}
ingredients = []

def permutations_w_constraints(n_perm_elements, sum_total, min_value, max_value):
    # base case
    if n_perm_elements == 1:
        if (sum_total <= max_value) & (sum_total >= min_value):
            yield (sum_total,)
    else:
        for value in range(min_value, max_value + 1):
            for permutation in permutations_w_constraints(
                n_perm_elements - 1, sum_total - value, min_value, max_value
            ):
                yield (value,) + permutation

def total_score(partition):
    capacity_sum = 0
    durability_sum = 0
    flavor_sum = 0
    texture_sum = 0
    calories_sum = 0

    for i in range(0, len(partition)):
        teaspoons = partition[i]
        capacity_sum += teaspoons * ingredient_info_dict[ingredients[i]][0]
        durability_sum += teaspoons * ingredient_info_dict[ingredients[i]][1]
        flavor_sum += teaspoons * ingredient_info_dict[ingredients[i]][2]
        texture_sum += teaspoons * ingredient_info_dict[ingredients[i]][3]
        calories_sum += teaspoons * ingredient_info_dict[ingredients[i]][4]

    if(calories_sum != 500):
        return 0

    result = [capacity_sum, durability_sum, flavor_sum, texture_sum]

    for i in range(0, len(result)):

        if(result[i] < 0):
            result[i] = 0

    return math.prod(result)

for i in range(0, len(my_list)):
    ingredient_info = my_list[i]
    match = list(parse_pattern.finditer(ingredient_info))[0]
    ingredient, capacity, durability, flavor, texture, calories = [match.group(x) for x in range(1, 7)]
    ingredients.append(ingredient)
    ingredient_info_dict[ingredient] = list(map(int, [capacity, durability, flavor, texture, calories]))

partitions = list(permutations_w_constraints(len(ingredients), 100, 1, 100))
partitions_perm = []

for p in partitions:

    for q in list(itertools.permutations(p)):
        partitions_perm.append(list(q))

print(max([total_score(p) for p in partitions_perm]))
