from aocd import get_data
import re

aunt_info_list = get_data(day=16, year=2015).split("\n")

remember_dict = {}
rememberstring ="""
children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""
rememberlist = rememberstring.split("\n")[1:]
parse_pattern_remember = re.compile(r'(\w+): (\d+)')

for i in range(0, len(rememberlist)):
    entry = rememberlist[i]
    match = list(parse_pattern_remember.finditer(entry))[0]
    item = match.group(1)
    amount = int(match.group(2))
    remember_dict[item] = amount

sues = []
parse_pattern_aunts = re.compile(r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)')

for i in range(0, len(aunt_info_list)):
    entry = aunt_info_list[i]
    match = list(parse_pattern_aunts.finditer(entry))[0]
    info_dict = {}
    info_dict[match.group(2)] = int(match.group(3))
    info_dict[match.group(4)] = int(match.group(5))
    info_dict[match.group(6)] = int(match.group(7))
    sues.append([int(match.group(1)), info_dict])

valid_sues = set(range(1, 501))

for item in remember_dict.keys():
    current_sue_set = set()

    for sue in sues:
        dict = sue[1]

        if(item not in dict.keys() or dict[item] == remember_dict[item]):
            current_sue_set.add(sue[0])
    valid_sues = set.intersection(valid_sues, current_sue_set)

print(list(valid_sues)[0])
