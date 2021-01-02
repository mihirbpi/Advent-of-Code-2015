from aocd import get_data
import itertools

my_list = list(map(int, get_data(day=17, year=2015).split("\n")))

def combinations(lst):
    combs = []

    for i in range(1, len(lst)+1):
        els = [list(x) for x in itertools.combinations(lst, i)]
        combs.extend(els)
    return combs

def num_combos(lst, combo_sum):
    combos_set = []
    all_combos = combinations(lst)

    for combo in all_combos:

        if(sum(combo) == combo_sum):
            combos_set.append(combo)

    return len(combos_set)

print(num_combos(my_list, 150))
