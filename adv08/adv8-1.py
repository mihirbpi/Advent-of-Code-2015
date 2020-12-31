from aocd import get_data
import re

my_list = get_data(day=8, year=2015).split("\n")

pattern_literal = re.compile(r'''
                             \\\\| # The double backslash (represents a backlash)
                             \\\"| # The backslash quote (represents a quote)
                             \\x[0-9|a-f]{2} # The backslash x followed by 2 hexadigits
                                             # (represents a character with that ascii code)
                             ''', re.X)
total_chars = 0
total_literal_chars = 0

for i in range(0, len(my_list)):
    string = my_list[i]
    total_chars += len(string)
    unquoted_string = string.strip('"')
    matches = pattern_literal.finditer(unquoted_string)
    replaced_string = re.sub(pattern_literal, "", unquoted_string)
    total_literal_chars += len(list(matches)) + len(replaced_string)

print(total_chars - total_literal_chars)
