from aocd import get_data

my_list = get_data(day=5, year=2015).split("\n")

def is_nice(string):
    if (any([x in string for x in ["ab", "cd", "pq", "xy"]])):
        return False

    vowels = list(filter(lambda x: x in 'aeiou', string))

    if(len(vowels) < 3):
        return False

    for i in range(0, len(string)):
        char = string[i]

        if(char * 2 in string):
            return True

    return False

count = 0

for i in range(0, len(my_list)):

    if(is_nice(my_list[i])):
        count += 1

print(count)
