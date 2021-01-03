from aocd import get_data
import numpy as np

number = int(int(get_data(day=20, year=2015))/10)
houses = np.zeros(number)

for i in range(1, number+1):
    houses[i:number:i] += 10 * i

print(np.nonzero(houses >= 10 * number)[0][0])
