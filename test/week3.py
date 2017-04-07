#compute process time and how many calls do we have
#computational complexity(Big O Notation)

# test = ['','world', 'a']
# print(test)
# print(test[::-1]

from time import process_time

#Computes the number of ordered ways to sum positive numbers such that they sum up to n.
#By ordered list we mean that e.g. to sum up to 3, we consider 1+2 and 2+1 to be different solutions.
def compute_number_of_ways(n):
    if n==0: #base case
        return 1
    else:
        sum = 0
        for i in range(0, n):
            sum += compute_number_of_ways(i)
        return sum
#Big O Notation of this function is?

#Same as compute_number_of_ways, but we implement memoization to save calls.
#Note that we check if the value has been computed at the beginning of the call.
#A different way consists in checking before making the recursive calls in the loop (you could try to implement this version at home)
def compute_number_of_ways_with_memoization(n, memory = {}):
    if n==0: #base case
        return 1
    elif n in memory: #"memoization" case: if this value has already been computed
        return memory[n]
    else: # we need to compute this value because it has not been computed
        sum = 0
        for i in range(0, n):
            sum += compute_number_of_ways_with_memoization(i, memory)
        memory[n] = sum
        return sum

#to test different methods we make a list of them that we can easily iterate on, to simplify testing.
# methods = [compute_number_of_ways, compute_number_of_ways_with_memoization]
# value = 25
# for method in methods:
#     start = process_time()
#     numberofways = method(value)
#     end = process_time()
#     print("Computing the number of ways ({}) to sum the value {} with the method {} took {} seconds".format(numberofways, value, method.__name__, end-start))

#Q1
#1.O(nlog(n))  O(n)
#2.O(n) faster

#Q2
#O(n^2)  O(n)



#Q4
def mystery(n):
    sum = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            sum += i
    return sum
# print(mystery(3))

#Q6
row1 = [None,0,1]
row2 = [1,None,1]
row3 = [0,0,None]
matrix = [row1, row2, row3]

def celebrityproblem(matrix):
    k = 0
    list = []
    for i in range(0, len(matrix)):
        if matrix[1][i] == 1:
            k = i

# print(celebrityproblem(matrix))


