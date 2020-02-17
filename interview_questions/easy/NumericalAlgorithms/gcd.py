"""find the gcd of two numbers"""

def gcd(a,b):
    while b >=0:
        if b == 0:
            return a
        else:
            rem = a % b
            return(gcd(b,rem))



print(gcd(64,4))
