from aocd import get_data

my_list = get_data(day=2, year=2015).split("\n")
total_length = 0

for i in range(0, len(my_list)):
    entry = my_list[i]
    dimensions = list(map(int, entry.split("x")))
    l, w, h = dimensions
    volume = l*w*h
    min_perim = min(2*(l+w), 2*(w+h), 2*(h+l))
    total_length += min_perim + volume

print(total_length)
