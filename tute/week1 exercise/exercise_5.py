# Q5

import random

x = random.randrange(1, 101, 1)
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
            elif z >= 10:
                print("That's way too high!")
            elif -10 < z < 0:
                print("That's too low!")
            elif z <= -10:
                print("That's way too low")
            count += 1
            y = int(input("Input guess: (0-100 inclusive):"))
            z = y - x

        print("Good Guess! It only took you %d tries" % count)
except Exception as e:
    print('Exception happened: ' + str(e))