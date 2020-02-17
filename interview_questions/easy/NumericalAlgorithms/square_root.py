def square_root(n):
    if n == 1:
        return 1
    else:
        return n ** 0.5


sqrt = square_root(16)
print("The square root is {}".format(round(sqrt,2)))
