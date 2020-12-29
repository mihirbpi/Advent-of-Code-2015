from aocd import get_data
import hashlib

key = get_data(day=4, year=2015)
i = 0

while True:
    to_hash = key + str(i)
    hash = hashlib.md5(to_hash.encode('utf-8')).hexdigest()

    if(hash.startswith("000000")):
        print(i)
        break

    i += 1
