'''
Created on Feb 28, 2017

@author: Richard's Surface
'''
import random

# 0, 1, 2 represent three doors
total = 100000
bingo = 0
bingoed_and_win = 0
not_bingoed_and_win = 0

for i in range(total):
    my_choice = random.choice([0, 1, 2])
    car = random.choice([0, 1, 2])
    switch = random.choice([True, False])
    if my_choice == car:
        bingo += 1
        if not switch:
            bingoed_and_win += 1
    else:
        if switch:
            not_bingoed_and_win += 1
        
print("%d times bingoed, rate is %.3f" %(bingo, 1.0 * bingo / total)) 
print("if you stay at your option, the time of getting car is %d, rate is %.3f" %(bingoed_and_win, 1.0 *bingoed_and_win / bingo)) 
print("if you change, the time of getting car is %d, rate is %.3f" %(not_bingoed_and_win, 1.0 *not_bingoed_and_win / total)     