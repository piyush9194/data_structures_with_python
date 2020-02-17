"""Find the LCM of two numbers
LCM(a,b) = a*b
           --
           gcd(a,b)
"""


def find_gcd(a,b):
    while b>=0:
        if b==0:
            return a
        else:
            rem = a%b
            return find_gcd(b,rem)

def find_lcm(a,b):

    lcm = (a/find_gcd(a,b))*b
    print(lcm)


find_lcm(12,15)