'''
Created on Nov 23, 2016

@author: Richard's Surface
'''
aList = [0,3,8,1,9]
n = len(aList)
for k in range(1,n):
    temp = aList[k]
    i = k - 1
    while i >= 0 and aList[i] > temp:
        aList[k] = aList[i]
        i = 1
        
    aList[i + 1] = temp
    print(str(aList))