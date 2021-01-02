from aocd import get_data
import re

my_list = get_data(day=14, year=2015).split("\n")
parse_pattern = re.compile(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')
reindeer_list = []
reindeer_info = {}

def find_distance(time, reindeer):
    speed = reindeer_info[reindeer][0]
    fly_interval = reindeer_info[reindeer][1]
    rest_interval = reindeer_info[reindeer][2]
    t = 0
    distance = 0
    resting = False
    time_travelling = 0
    time_resting = 0

    while(t <= time):

        if(not resting):

            distance += speed
            time_travelling += 1

            if(time_travelling == fly_interval):
                resting = True
                time_travelling = 0

        elif(resting):

            time_resting += 1

            if(time_resting == rest_interval):
                resting = False
                time_resting = 0
        t += 1

    return distance

for i in range(0, len(my_list)):
    rule = my_list[i]
    match = list(parse_pattern.finditer(rule))[0]
    reindeer = match.group(1)
    speed = int(match.group(2))
    fly_interval = int(match.group(3))
    rest_interval = int(match.group(4))
    reindeer_list.append(reindeer)
    reindeer_info[reindeer] = [speed, fly_interval, rest_interval]

distances  = [find_distance(2503, reindeer) for reindeer in reindeer_list]
print(max(distances))
