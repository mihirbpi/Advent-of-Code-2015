from aocd import get_data

my_list = get_data(day=2, year=2015).split("\n")
total_area = 0

for i in range(0, len(my_list)):
    entry = my_list[i]
    dimensions = list(map(int, entry.split("x")))
    l, w, h = dimensions
    slack = min(l*w, w*h, h*l)
    total_area += 2*l*w + 2*w*h + 2*h*l + slack

print(total_area)
