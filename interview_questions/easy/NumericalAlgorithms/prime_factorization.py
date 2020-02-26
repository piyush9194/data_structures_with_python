"""Find the prime factorization of a given number"""
import math

def prime_factors(num):
    result = ""
    while num >1:
        for i in range(2,int(math.sqrt(num)),2):
            while (num%i) == 0:
                result = result + str(i) + "*"
                num = int(num/i)
        if num != 1:
            result = result + str(num)
            break
    return result




print(prime_factors(64))
