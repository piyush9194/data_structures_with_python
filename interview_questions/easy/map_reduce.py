import re

def map(data):
    map_out = []
    words= re.findall(r"[\w']+", data)
    for item in words:
        map_out.append([item,1])
    print(f" the output of map phase is {map_out}")
    reduce(map_out)


def reduce(data):
    reduce_out = {}
    for item in data:
        key = item[0]
        value = item[1]
        if key not in reduce_out:
            reduce_out[key] = value
        else:
            reduce_out[key] = reduce_out[key] + 1
    print(f" the output of reduce phase is {reduce_out}")

data = "i am the. the words; the i am"
map(data)