def binary_search(item, data):
    print(data)
    start = 0
    end = len(data)-1

    middle = int(len(data)/2)
    print(middle)

    if len(data) == 0:
        print("Item not found")
    elif item == data[middle]:
        print("Item found")
    elif item > data[middle]:
        start = middle +1
        binary_search(item,data[start:])
    elif item < data[middle]:
        end = middle
        binary_search(item,data[:end])


binary_search(1,[])
