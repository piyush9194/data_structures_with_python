def factorial(n):
    if n in (1,0):
        return 1
    else:
        return (n*factorial(n-1))

num= 8
result=factorial(num)
print("the factorial of {} is {} ".format(num,result))