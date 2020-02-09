def hammingDistance( x, y):
    def get_binary(x):
        str_a = []
        while (x > 0):
            a = x % 2
            x = int(x / 2)
            str_a.append(a)
        return (str_a)

    str_1 = get_binary(x)
    str_2 = get_binary(y)

    if x > y:
        for i in range(0, len(str_1) - len(str_2)):
            str_2.append(0)
    else:
        for i in range(0, len(str_2) - len(str_1)):
            str_1.append(0)
    count = 0
    print(str_1, str_2)
    for i in range(0, len(str_1)):
        if str_1[i] != str_2[i]:
            count = count + 1

    print(count)


hammingDistance(2,4)