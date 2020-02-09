def find_duplicates(data):
    dict ={}
    for item in data:
        if item not in dict.keys():
            dict[item]= 1
        else:
            dict[item] = dict[item]+ 1
    for k,v in dict.items():
        if v>1:
            print("the {} occured {} times".format(k,v))


find_duplicates([1,2,3,4,5,4,4,4,3])

