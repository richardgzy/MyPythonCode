# Q1

# name = input("Please input your name:")
# print("Welcome, %s" % name)

# #Q2

# try:
#     number = int(input("Please input a integer:"))
#     if number % 2 != 0:
#         print("%d is even" % number)
#     elif number % 2 == 0:
#         print("%d is odd" % number)
# except Exception as e:
#     print('Exception happened: ' + str(e))

# Q3

# try:
#     i = int(input("Please input a number to do factorial calculation:"))
#     sum = 1
#     for x in range(2, i + 1):
#         sum = x * sum
#     print("The factorial number is %d" % sum)
# except Exception as e:
#     print('Exception happened: ' + str(e))

# Q4

# dic = {"01" : "January", "02" : "Feburary", "03" : "March", "04" : "April", "05" : "May"\
#     , "06" : "June", "07" : "July", "08" : "August", "09" : "September", "10" : "Octotber"\
#        , "11" : "November", "12" : "December"}
# input = input("Please input a date in format DD/MM/YYYY:")
# stringset = input.split("/")
# if stringset[0] not in (1, 32) or stringset[1] not in (1, 13): # how to validate the year?
#     print("Invalid Input")
# else:
#     month = dic[stringset[1]]
#     date = stringset[0]
#     year = stringset[2]
#     print("%s %s %s" % (month, date, year))

# Q5
# import random
#
# x = random.randrange(1, 101, 1)
# try:
#     y = int(input("Input guess (0-100 inclusive):"))
#     if y not in range(0, 101):
#        print("Invalid input, Please choose number in 0-100 inclusive")
#     else:
#         z = y - x
#         count = 1
#         while z != 0:
#             if 0 < z < 10:
#                 print("That's too high!")
#             elif z >= 10:
#                 print("That's way too high!")
#             elif -10 < z < 0:
#                 print("That's too low!")
#             elif z <= -10:
#                 print("That's way too low")
#             count += 1
#             y = int(input("Input guess: (0-100 inclusive):"))
#             z = y - x
#
#         print("Good Guess! It only took you %d tries" % count)
# except Exception as e:
#     print('Exception happened: ' + str(e))

# Q6

# result = 1
# try:
#     n = int(input("Please input a positive integer:"))
#     for i in range(0, n + 1):
#         if i <= 0:
#             result = 1
#         elif i >= 1 and i % 2 == 0:
#                 result = result + i
#         elif i >= 1 and i % 2 == 1:
#                 result = result * i
#     print(result)
# except Exception as e:
#     print('Exception happened: ' + str(e))

# Q7
import random

x = random.randrange(1, 101, 1)
aList = []
for i in range(1, 101):
    aList.append(i)

# function for finding an item's index in a List. if not found, return None
def findindexinlist(x, aList):
    for i in range(1, len(aList)):
        if aList[i] == x:
            return i
    return None

try:
    y = int(input("Input guess (0-100 inclusive):"))
    if y not in range(0, 101):
        print("Invalid input, Please choose number in 0-100 inclusive")
    else:
        z = y - x
        count = 1
        while z != 0:
            if 0 < z < 10:
                print("That's too high!")
                tempindex = findindexinlist(y, aList)
                aList = aList[:tempindex]
            elif z >= 10:
                print("That's way too high!")
                tempindex = findindexinlist(y, aList)
                aList = aList[:(tempindex - 10)]
            elif -10 < z < 0:
                print("That's too low!")
                tempindex = findindexinlist(y, aList)
                aList = aList[(tempindex + 1):]
            elif z <= -10:
                print("That's way too low")
                tempindex = findindexinlist(y, aList)
                aList = aList[(tempindex + 10):]
            print("Guess in", aList)
            count += 1
            y = int(input("Input guess: (0-100 inclusive):"))
            z = y - x

        print("Good Guess! It only took you %d tries" % count)
except Exception as e:
    print('Exception happened: ' + str(e))



