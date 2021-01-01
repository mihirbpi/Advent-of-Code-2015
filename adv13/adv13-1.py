from aocd import get_data
import re
import itertools

my_list = get_data(day=13, year=2015).split("\n")
parse_pattern = re.compile(r'(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).')
happiness_dict = {}
people_set = set()

def circ_perm(lst):
    gen = itertools.permutations(lst[1:])

    for end in gen:
        yield [lst[0]] + list(end)

def total_happiness_change(lst, happiness_dict):
    change = 0

    for i in range(0, len(lst)):
        person = lst[i]
        neighbor1 = lst[(i-1) % len(lst)]
        neighbor2 = lst[(i+1) % len(lst)]

        if((person, neighbor1) in happiness_dict.keys()):
            change += happiness_dict[(person, neighbor1)]

        if((person, neighbor2) in happiness_dict.keys()):
            change += happiness_dict[(person, neighbor2)]

    return change

for i in range(0, len(my_list)):
    rule = my_list[i]
    match = list(parse_pattern.finditer(rule))[0]
    person = match.group(1)
    increase = match.group(2)
    amount = int(match.group(3))

    if(increase == "lose"):
        amount *= -1

    next_to_person = match.group(4)
    happiness_dict[(person, next_to_person)] = amount
    people_set.add(person)

people_list = list(people_set)
arrangments = list(circ_perm(people_list))
print(max([total_happiness_change(lst, happiness_dict) for lst in arrangments]))
