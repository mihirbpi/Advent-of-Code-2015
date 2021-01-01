from aocd import get_data
import re

curr_password = get_data(day=11, year=2015).split("\n")[0]

pattern_pair = re.compile(r'([a-z])\1')
consecutive_list = []

for i in range(1, 25):
    consecutive_list.append(chr(96+i) + chr(97+i)+ chr(98+i))

def increment(string):
    string_list = [x for x in string]
    index = len(string_list) - 1

    if(string_list[index] != "z"):
        string_list[index] = chr(ord(string_list[index])+1)

    else:
        string_list[index] = "a"

        while(string_list[index] == "a"):
            index -= 1

            if(string_list[index] != "z"):
                string_list[index] = chr(ord(string_list[index])+1)

            else:
                string_list[index] = "a"

    return "".join(string_list)

def contains_two_different(password):
    track_set = set()

    for i in range(0, len(password)-1, 1):

        if(password[i] == password[i+1]):
            track_set.add(password[i] + password[i+1])

    return(len(track_set) > 1)

def is_valid(password):
    
    if ("i" in password or "o" in password or "l" in password):
        return False

    matches = pattern_pair.finditer(password)

    if (not contains_two_different(password)):
        return False

    for consecs in consecutive_list:

        if(consecs in password):
            return True

    return False

curr_password = increment(curr_password)

while (not is_valid(curr_password)):
    curr_password = increment(curr_password)

curr_password = increment(curr_password)

while (not is_valid(curr_password)):
    curr_password = increment(curr_password)

print(curr_password)
