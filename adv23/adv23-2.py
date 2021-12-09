
from aocd import get_data

input = get_data(day=23, year=2015).split("\n")
reg_dict = {"a": 1, "b": 0}

pc = 0

while(pc < len(input)):
    line = input[pc]
    command, first_input, second_input = 3*[None]

    if(len(line.split(" ")) == 2):
        command, first_input = line.split(" ")

    elif(len(line.split(" ")) == 3):
        command, first_input, second_input = line.split(" ")

    first_input = first_input.strip(",")

    if(first_input[0] == "+"):
        first_input = int(first_input[1:])

    elif(first_input[0] == "-"):
        first_input = -1*int(first_input[1:])

    if(second_input != None and second_input[0] == "+"):
        second_input = int(second_input[1:])

    elif(second_input != None and second_input[0] == "-"):
        second_input = -1*int(second_input[1:])

    if(command == "hlf"):
        reg_dict[first_input] = reg_dict[first_input]/2
        pc += 1

    elif(command == "tpl"):
        reg_dict[first_input] *= 3
        pc += 1

    elif(command == "inc"):
        reg_dict[first_input] += 1
        pc += 1

    elif(command == "jmp"):
        pc += first_input

    elif(command == "jie"):

        if(reg_dict[first_input] % 2 == 0 ):
            pc += second_input
            
        else:
            pc += 1

    elif(command == "jio"):

        if(reg_dict[first_input] == 1):
            pc += second_input

        else:
            pc += 1

print(reg_dict["b"])
