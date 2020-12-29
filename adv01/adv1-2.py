from aocd import get_data

my_list = get_data(day=1, year=2015)

floor = 0

for i in range(0, len(my_list)):
    instruction = my_list[i]

    if(instruction == "("):
        floor += 1

    elif(instruction == ")"):
        floor -= 1

    if(floor == -1):
        print(i + 1)
        break
