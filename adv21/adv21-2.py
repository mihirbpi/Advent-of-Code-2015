from aocd import get_data
import re
import itertools
import copy

my_list = get_data(day=21, year=2015).split("\n")
boss_stats_orig = [int(my_list[0].split(" ")[2]), int(my_list[1].split(" ")[1]), int(my_list[2].split(" ")[1])]
you_stats_orig = [100, 0, 0]

parse_pattern_items = re.compile(r'(\w+)(\s+)(\d+)(\s+)(\d+)(\s+)(\d+)')
weapons_string="""
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0"""
weapons_list = weapons_string.split("\n")[1:]
weapons_dict = {}

for i in range(0, len(weapons_list)):
    info = weapons_list[i]
    match = list(parse_pattern_items.finditer(info))[0]
    name, cost, damage, armor = [match.group(1), int(match.group(3)), int(match.group(5)), int(match.group(7))]
    weapons_dict[name] = [cost, damage, armor]

armor_string="""
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5"""
armor_list = armor_string.split("\n")[1:]
armor_dict = {}

for i in range(0, len(armor_list)):
    info = armor_list[i]
    match = list(parse_pattern_items.finditer(info))[0]
    name, cost, damage, armor = [match.group(1), int(match.group(3)), int(match.group(5)), int(match.group(7))]
    armor_dict[name] = [cost, damage, armor]

rings_string="""
DamageOne    25     1       0
DamageTwo    50     2       0
DamageThree   100     3       0
DefenseOne   20     0       1
DefenseTwo   40     0       2
DefenseThree   80     0       3"""
rings_list = rings_string.split("\n")[1:]
rings_dict = {}

for i in range(0, len(armor_list)):
    info = rings_list[i]
    match = list(parse_pattern_items.finditer(info))[0]
    name, cost, damage, armor = [match.group(1), int(match.group(3)), int(match.group(5)), int(match.group(7))]
    rings_dict[name] = [cost, damage, armor]

def cost(items_choice, weapons_dict, armor_dict, rings_dict):
    amount = 0
    weapons_list = items_choice[0]
    armors_list = items_choice[1]
    rings_list = items_choice[2]

    for weapon in weapons_list:
        amount += weapons_dict[weapon][0]

    for armor in armors_list:
        amount += armor_dict[armor][0]

    for ring in rings_list:
        amount += rings_dict[ring][0]

    return amount

def does_win(items_choice, weapons_dict, armor_dict, rings_dict, boss_stats_orig, you_stats_orig):
    you_stats = copy.deepcopy(you_stats_orig)
    boss_stats = copy.deepcopy(boss_stats_orig)
    weapons_list = items_choice[0]
    armors_list = items_choice[1]
    rings_list = items_choice[2]

    for weapon in weapons_list:
        you_stats[1] += weapons_dict[weapon][1]
        you_stats[2] += weapons_dict[weapon][2]

    for armor in armors_list:
        you_stats[1] += armor_dict[armor][1]
        you_stats[2] += armor_dict[armor][2]

    for ring in rings_list:
        you_stats[1] += rings_dict[ring][1]
        you_stats[2] += rings_dict[ring][2]

    you_hitpts, you_damage, you_armor = you_stats
    boss_hitpts, boss_damage, boss_armor = boss_stats
    turn = "player"

    while(True):

        if(turn == "player"):
            damage_dealt = max(1, you_damage - boss_armor)
            boss_hitpts -= damage_dealt

            if(boss_hitpts <= 0):
                winner = "you"
                break

            turn = "boss"

        elif(turn == "boss"):
            damage_dealt = max(1, boss_damage - you_armor)
            you_hitpts -= damage_dealt

            if(you_hitpts <= 0):
                winner = "boss"
                break

            turn = "player"

    return winner == "you"

numbers = list(itertools.product([1], [0, 1], [0, 1, 2]))
costs = []

for number_choice in numbers:
    number_choice_list = list(number_choice)
    num_weapons = number_choice_list[0]
    num_armors = number_choice_list[1]
    num_rings = number_choice_list[2]
    weapons = list(map(list, list(itertools.combinations(list(weapons_dict.keys()), num_weapons))))
    armors = list(map(list, list(itertools.combinations(list(armor_dict.keys()), num_armors))))
    rings = list(map(list, list(itertools.combinations(list(rings_dict.keys()), num_rings))))
    items_choice_list = list(map(list, list(itertools.product(weapons, armors, rings))))

    for items_choice in items_choice_list:

        if(not does_win(items_choice, weapons_dict, armor_dict, rings_dict, boss_stats_orig, you_stats_orig)):
            costs.append(cost(items_choice, weapons_dict, armor_dict, rings_dict))

print(max(costs))
