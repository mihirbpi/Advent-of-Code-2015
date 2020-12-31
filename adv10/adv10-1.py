from aocd import get_data

string = get_data(day=10, year=2015)

def new_string(string):
    l = []
    current_digit = string[0]
    count = 0

    for i in range(0, len(string)):
        char = string[i]

        if(char == current_digit):
            count += 1

        elif(char != current_digit):
            l.append([str(count), current_digit])
            count = 1
            current_digit = char

    l.append([str(count), current_digit])
    return "".join(["".join(x) for x in l])

for i in range(0, 40):
    string = new_string(string)

print(len(string))
