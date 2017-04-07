#Q1
# def product(x, y):
#     if x == 0 or y == 0:
#         return 0
#     else:
#         return x + product(x, y - 1)
# # Test
# print(product(2, 3))


#Q2
def bisectionitr(l, x):
    lb = 0
    ub = len(l) - 1
    while len(l) != 2:
        mid = (lb + ub)//2
        if l[mid] <= x:
            lb = mid + 1
        else:
            ub = mid - 1
        l = l[l[lb]:l[ub]]
    if lb == x or ub == x:
        return True
    else:
        return False

#Q3
def biosectionrec(l, x, lb, ub):
    if lb >= ub: #prevent lb > ub
        return False
    if len(l) == 0: # if the list is empty return false
        return False
    if x == l[lb] or x == l[ub]: # check the boundary value
        return True
    if ub - lb == 1:
    # in this case, there are only two value in list
    # and neither of them is x
        return False

    mid = (lb + ub)//2
    if x == l[mid]:
        return True
    elif x > l[mid]:
        return biosectionrec(l, x, mid + 1, ub)
    else:
        return biosectionrec(l, x, lb, mid - 1)

#Test
l = [1, 4, 7]
empty = []
# print(biosectionrec(l, 5, 0, len(l) - 1))
# print(bisectionrec(l, 2, 0, len(l)))
# print()


#Q4

def fibonnachiitr(x):
    result = [1, 1]
    if x > 2:
        for i in range(2, x):
            result.append(result[i - 2] + result[i - 1])
        return result[x - 1]
    else:
        return 1

# print(fibonnachiitr(6))

#Q5

import timeit

#expontential complexity
def fibonnachirec(x):
    if x > 2:
        return fibonnachirec(x - 1) + fibonnachirec(x - 2)
    else:
        return 1

#Q6

def fibonnachirecwithmemo(x):
    dict = {0: 1, 1: 1}
    if x < 3:
        return 1
    elif x == len(dict):
        temp = dict.get(x - 1) + dict.get(x - 2)
        dict[x - 1] = temp
        return temp
    elif x == len(dict) + 1:
        temp = dict.get(x - 2) + fibonnachirecwithmemo(x - 1)
        dict[x - 1] = temp
        return temp
    elif x > len(dict) + 1:
        temp = fibonnachirecwithmemo(x - 2) + fibonnachirecwithmemo(x - 1)
        dict[x - 1] = temp
        return temp

def memo2(n, memory = {}):
    if n == 0:
        return 1
    elif n in memory:
        return memory[n]
    else:
        sum = 0
        for i in range(1, n):
            sum += memo2(i, memory)
        memory[n] = sum
        return sum


start1 = timeit.default_timer()
print(fibonnachirecwithmemo(10))
stop1 = timeit.default_timer()
print("running time for memorization is %.10f second" % (stop1 - start1))

start2 = timeit.default_timer()
print(fibonnachirec(10))
stop2 = timeit.default_timer()
print("running time for regular recursion is %.10f second" % (stop2 - start2))

start3 = timeit.default_timer()
print(memo2(10))
stop3 = timeit.default_timer()
print("running time for lecturer's memo is %.10f second" % (stop3 - start3))


#Q7
import math
def squareroot(x):# .1f edition
    temp = 0
    temp2 = 0
    for i in range(0, 10):
        if i ** 2 == x:
            return i
        elif i ** 2 > x:
            temp = i - 1
            break

    for i in range(0, 10):
        temp2 = temp + i / 10
        if temp2 ** 2 == x:
            return temp2
        elif temp2 ** 2 > x:
            return temp + (i - 1)/10 * 1

# def squarerootusingbiosec(x):


# print(squareroot(10))
# print(math.sqrt(10))