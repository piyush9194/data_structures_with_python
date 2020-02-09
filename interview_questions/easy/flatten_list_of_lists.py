def flatten(list):
    final_list = []

    for items in list:
        for element in items:
            final_list.append(element)


    print(final_list)


flatten([[1,2,3],[5,6,7],[  ]])