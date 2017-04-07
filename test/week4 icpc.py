
def GCD(x,y):
    if y==0:
        return x
    elif x%y == 0:
        return x%y
    else:
        return GCD(x, x%y)
from fractions import gcd

# print(GCD(20,16))
# print(gcd(20,16))



## O(sqrt(n))!!!  factorlization
# import math
#
# n = 24
# for i in range(2,int(math.sqrt(n))):
#     if(n%i == 0):
#         while(n%i == 0):
#             print(i)
#             n /= i

##print prime numbers
##O(log(min(m,n))) !!!!
# def gcd(m,n):
#     if n==0:
#         return m
#     else:
#         return gcd(n, m%n)
#
# print(gcd(32,24))



##O(log(n))
def power(base, expo):
    if expo == 0:
        return 1
    elif expo % 2 == 0:
        res = power(base, expo/2)
        ##res = res * res
    elif expo % 2 ==1:
        res *= base
        return res

## add mod param and % to each times function to optimize
def power2(base, expo, mod):
    if expo == 0:
        return 1%mod
    res = power2(base, expo/2)
    res = res * res % mod
    if expo % 2 ==1:
        res = base * res % mod
        return res

print(power(7, 10000000))

## in c++ negative number% n gonna be the negative number, but in python its positive