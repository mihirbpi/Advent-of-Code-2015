from aocd import get_data
from collections import defaultdict

input = get_data(day=25, year=2015).split("\n")

input_row = int(input[0].split(" ")[-3].strip(","))
input_col = int(input[0].split(" ")[-1].strip("."))
table = defaultdict(lambda:-1)
table[(1, 1)] = 20151125
row, col = [1, 1]

while(not (row == input_row and col == input_col)):
    temp = table[(row, col)]

    if(row == 1):
        row = col + 1
        col = 1
    else:
        row -= 1
        col += 1

    table[(row, col)] = temp * 252533 % 33554393

print(table[(input_row, input_col)])
