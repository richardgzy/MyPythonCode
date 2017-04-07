'''
Created on Feb 21, 2017

@author: Richard's Surface
'''
def findMin(aList):
    minSoFar = aList[0]
    for i in aList:
        if (i < minSoFar):
            minSoFar = i
    return minSoFar

def sortList (aList):
    sortedList = []
    while (aList != []):
        min1 = findMin(aList)
        sortedList.append(min1)
        aList.remove(min1)
    return sortedList

print(sortList([3,10,5,9,8,0,0]))