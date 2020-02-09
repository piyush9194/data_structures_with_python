"""Remove duplicates from the list while mainatining the order"""



def remove_dups(list):
    set_a = set()

    for item in list:
        if item not in set_a:
            set_a.add(item)
    return set_a



data = [1,2,3,1,4,1,5,6,78,2,3]
out=remove_dups(data)
print(list(out))



