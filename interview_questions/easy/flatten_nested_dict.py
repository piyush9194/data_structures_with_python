out_dict = {}

def flatten_dict(data):
    for k, v in data.items():
        if type(v) is dict:
            flatten_dict(v)
        else:
            out_dict[k] = v
            print(out_dict)

data ={'a': 1,
 'c': {'a': 2,
       'b': {'x': 5,
             'y' : 10}},
 'd': [1, 2, 3]
       }

flatten_dict(data)
