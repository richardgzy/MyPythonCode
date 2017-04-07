'''
Created on Feb 23, 2017

@author: Richard's Surface
'''
#Test from Lecturer
#Q1

# name = input("Please input your name:")
# print("Welcome, " + name)


#Q2
  
# x = input("Please input an integer:")
# x = int(x)
# if x % 2 == 0:
#     print(x,"is even")
# else:
#     print(x,"is odd")

#Q3

# def printFactorialNumber(n):
#     factorial = 1
#     if n < 0:
#         print("invalid input")
#     else:
#         for i in range(1, n+1):
#             factorial *= i
#     print(factorial)
#  
# printFactorialNumber(10)







#Test 2016
#Q1

# def printSquareNumbers(n):
#     for i in range(0, n+1):
#         print(i ** 2)
#
# printSquareNumbers(6)

#Q2
# def printFactorialNumberUsingRecursion(n):
#     if n == 0:
#         return 1
#     else:
#         return n * printFactorialNumberUsingRecursion(n-1)
# 
# print(printFactorialNumberUsingRecursion(2))

# the function I wrote use recursion algorithm because it takes less time to execute.
# The function does not have much looping and assignment



#Q3
# import math
#  
# n = int(input("Please input an integer bigger than 1:"))
# A = []
# result = []
#  
#  
# if n <= 1:
#     print("invalid input")
# else:
#     for i in range(0, n+1):
#         A.append(True)
# for i in range(2, int(math.sqrt(n))):
#     if A[i] == True:
#         for j in range(i**2, n, i):
#             A[j] = False
#  
# for i in range(2, n+1):
#     if A[i] == True:
#         result.append(i)
#  
# print(result)
#Q4

# def findMaxiNumberinList(aList):
#     if len(aList) == 1:
#             return  aList[0]
#     else:
#         max = findMaxiNumberinList(aList[1:])
#         if max > aList[0]:
#             return max
#         else:
#             return aList[0]
# 
# print(findMaxiNumberinList([1,2,3,1,999,8]))

#Q5
  
# request = []
# num = len(request)
#   
# #a
# # the request starts with 1
# def newRequest():
#     if num == 0:
#         request.append(1)
#     else:
#         request.append(num + 1)
#   
# #b   
# #assume the request served will be marked as 0 instead of the integer given
# #
# def solveRequest():
#     for i in range(0, len(request)):
#         if request[i] != 0:
#             request[i] = 0
#             return
#     print("There is no request to be served")
# 
# def servedRequestSoFar():
#     servedSoFar = 0
#     for i in range(0, num):
#         if request[i] != 0:
#             servedSoFar = i
#             return servedSoFar
#     servedSoFar = None
#     return servedSoFar
#  
# def printNextRequestToServe():
#     servedSoFar = servedRequestSoFar()
#     if servedSoFar == None:
#         print("There is no unserved request")
#     else:
#         print("The next request waiting is ", servedSoFar)
# 
# #add 3 requests to list:
# newRequest()
# newRequest()
# newRequest()
# 
# # solve a request:
# solveRequest()
# 
# #show next request to be served:
# 
# printNextRequestToServe()




    
#Q6

# class Shape:
#     
#     def __init__(self, area):
#         self.area = area
#     
#     def setArea(self, area):
#         self.area = area
#     
#     def getArea(self):
#         return self.area
# 
# import math
# class Circle(Shape):
#     
#     def __init__(self, radius):
#         self.area = radius ** 2 * math.pi
#     
#     def getRadius(self):
#         return self.radius
#     
#     def setRadius(self, radius):
#         self.radius = radius
#         self.area = radius ** 2 * math.pi
#     
# class Square(Shape):
#     
#     def __init__(self, sidelength):
#         self.area = sidelength ** 2
#     
#     def getSidelength(self):
#         return self.sidelength
#     
#     def setSidelength(self, sidelength):
#         self.sidelength = sidelength
#         self.area = sidelength ** 2
# 
# circle1 = Circle(1)
# print(circle1.getArea())

request = []
req_no = 1

def create():
    request.append(req_no)
    req_no += 1

create()

