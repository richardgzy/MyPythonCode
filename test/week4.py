aList = [32, 54, 16, 16, 0, 25, 98]

##Bubble Sort
changed = True
l = len(aList)
while changed:
    changed = False
    for i in range(0, l-1):
        if aList[i] > aList[i+1]:
            aList[i], aList[i+1] = aList[i+1], aList[i]
            changed = True
    l -= 1
print(aList)

##Merge Sort
