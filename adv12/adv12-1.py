from aocd import get_data
import re

data = get_data(day=12, year=2015)
number_pattern = re.compile(r'-?\d+')
matches = number_pattern.finditer(data)
sum = 0

for match in matches:
    sum += int(data[match.span()[0]:match.span()[1]])

print(sum)
