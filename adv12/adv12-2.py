from aocd import get_data
import json

data = get_data(day=12, year=2015).replace("\n","")
data_json = json.loads(data)

def sum_of(data_json):

    if(isinstance(data_json, list)):
        return sum([sum_of(x) for x in data_json])

    if(isinstance(data_json, dict)):

        if('red' in data_json.values()):
            return 0

        else:
            return sum([sum_of(x) for x in data_json.values()])

    if(isinstance(data_json, int)):
        return data_json

    else:
        return 0

print(sum_of(data_json))
