from aocd import get_data
from collections import defaultdict

my_list = get_data(day=6, year=2015).split("\n")
lights_dict = defaultdict(lambda: 0)

for i in range(0, len(my_list)):
    command = my_list[i]
    split_command = command.split(" ")
    action = ""
    start_coords = 0
    end_coords = 0

    if(split_command[0] == "toggle"):
        action = split_command[0]
        start_coords = tuple(map(int, split_command[1].split(",")))
        end_coords = tuple(map(int, split_command[3].split(",")))

    elif(split_command[0] == "turn"):
        action = split_command[0] + split_command[1]
        start_coords = tuple(map(int, split_command[2].split(",")))
        end_coords = tuple(map(int, split_command[4].split(",")))

    start_row = start_coords[0]
    end_row = end_coords[0]
    start_column = start_coords[1]
    end_column = end_coords[1]

    for row in range(start_row, end_row + 1):

        for column in range(start_column, end_column + 1):
            light = (row, column)

            if(action == "toggle"):
                lights_dict[light] = lights_dict[light] + 2

            elif(action == "turnon"):
                lights_dict[light] = lights_dict[light] + 1

            elif(action == "turnoff"):

                if(lights_dict[light] > 0):
                    lights_dict[light] = lights_dict[light] - 1

brightness = 0

for light in lights_dict.keys():
    brightness += lights_dict[light]

print(brightness)
