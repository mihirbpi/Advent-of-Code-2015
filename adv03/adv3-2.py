from aocd import get_data

my_list = get_data(day=3, year=2015)
houses_dict = {(0, 0): 2}

curr_santa_x = 0
curr_santa_y = 0
curr_robosanta_x = 0
curr_robosanta_y = 0

for i in range(0, len(my_list) - 1, 2):
    instruction_santa = my_list[i]
    instruction_robosanta = my_list[i+1]

    if(instruction_santa == "^"):
        curr_santa_y += 1

    elif(instruction_santa == "v"):
        curr_santa_y -= 1

    elif(instruction_santa == ">"):
        curr_santa_x += 1

    elif(instruction_santa == "<"):
        curr_santa_x -= 1

    if((curr_santa_x, curr_santa_y) in houses_dict.keys()):
        houses_dict[(curr_santa_x, curr_santa_y)] += 1

    else:
        houses_dict[(curr_santa_x, curr_santa_y)] = 1

    if(instruction_robosanta == "^"):
        curr_robosanta_y += 1

    elif(instruction_robosanta == "v"):
        curr_robosanta_y -= 1

    elif(instruction_robosanta == ">"):
        curr_robosanta_x += 1

    elif(instruction_robosanta == "<"):
        curr_robosanta_x -= 1

    if((curr_robosanta_x, curr_robosanta_y) in houses_dict.keys()):
        houses_dict[(curr_robosanta_x, curr_robosanta_y)] += 1

    else:
        houses_dict[(curr_robosanta_x, curr_robosanta_y)] = 1

print(len(houses_dict.keys()))
