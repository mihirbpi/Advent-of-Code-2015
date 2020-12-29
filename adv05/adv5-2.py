from aocd import get_data
import re

my_list = get_data(day=5, year=2015).split("\n")

def is_nice(string):

    b1 = False
    for i in range(0, len(string) - 2):

        if(string[i] == string[i+2]):
            b1 = True

    if(not b1):
        return False

    b2 = False

    for i in range(0, len(string) - 1):
        seq = string[i] + string[i+1]
        indices = tuple([m.start() for m in re.finditer(seq, string)])

        if(len(indices) >= 2):
            b2 = True

    if(not b2):
        return False

    return True

count = 0

for i in range(0, len(my_list)):

    if(is_nice(my_list[i])):
        count += 1

print(count)
