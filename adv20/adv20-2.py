from aocd import get_data
import numpy as np

number = int(get_data(day=20, year=2015))
houses = np.zeros(1000000)

for i in range(1, 1000000):
    houses[i:i * 50:i] += 11 * i

print(np.nonzero(houses >= number)[0][0])
