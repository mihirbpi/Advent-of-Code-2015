from aocd import get_data

my_list = get_data(day=8, year=2015).split("\n")

total_chars = 0
total_updated_chars = 0

for i in range(0, len(my_list)):
    string = my_list[i]
    total_chars += len(string)
    replaced_string_backlash = string.replace("\\", "\\\\")
    replaced_string_quote = string.replace("\"", "\\\"")
    total_updated_chars += 2 + len(string) + len(replaced_string_backlash) + len(replaced_string_quote) - (2*len(string))

print(total_updated_chars - total_chars)
