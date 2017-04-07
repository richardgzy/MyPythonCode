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