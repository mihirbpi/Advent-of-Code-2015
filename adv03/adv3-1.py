from aocd import get_data

my_list = get_data(day=3, year=2015)
houses_dict = {(0, 0): 1}

curr_x = 0
curr_y = 0

for i in range(0, len(my_list)):
    instruction = my_list[i]

    if(instruction == "^"):
        curr_y += 1

    elif(instruction == "v"):
        curr_y -= 1

    elif(instruction == ">"):
        curr_x += 1

    elif(instruction == "<"):
        curr_x -= 1

    if((curr_x, curr_y) in houses_dict.keys()):
        houses_dict[(curr_x, curr_y)] += 1

    else:
        houses_dict[(curr_x, curr_y)] = 1

print(len(houses_dict.keys()))
