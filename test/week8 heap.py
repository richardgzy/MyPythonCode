class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    # sorting(pecolating) the heap after insert
    def percUpforMinHeap(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def percUpforMaxHeap(self, i):
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    # insert a value to the last position of heap and do the sort
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUpforMinHeap(self.currentSize)

    # sorting(pecolating) the heap after insert
    def percDownForMinHeap(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def percDownForMaxHeap(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.maxChild(i)
            if self.heapList[i] < self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    # find the minimun child in a smallest b-tree
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    # find the maximun child in a smallest b-tree
    def maxChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] > self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    # delete the min valiue and return it
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDownForMinHeap(1)
        return retval

    # delete the max valiue and return it
    def delMax(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDownForMaxHeap(1)
        return retval

    # convert a list to minheap
    def buildMinHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDownForMinHeap(i)
            i = i - 1
        return self.heapList

    # convert a list to maxheap
    def buildMaxHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDownForMaxHeap(i)
            i = i - 1
        return self.heapList

    # given an index of node, both the child of it are maxheap, make the hole tree a maxheap
    def maxheapify(self, i):
        if 2*i > self.currentSize or 2*i +1 > self.currentSize:
            return self.heapList
        if self.heapList[i] >= self.heapList[self.maxChild(i)]:
            return self.heapList
        else:
            if self.heapList[2 * i] >= self.heapList[2 * i + 1]:
                self.heapList[i], self.heapList[2 * i] = self.heapList[2 * i], self.heapList[i]
                self.maxheapify(2 * i)
            elif self.heapList[2 * i] > self.heapList[2 * i + 1]:
                self.heapList[i], self.heapList[2 * i + 1] = self.heapList[2 * i + 1], self.heapList[i]
                self.maxheapify(2 * i + 1)
            else:
                return self.heapList

            return self.heapList

##
def BuildMaxHeap(L):
    a = BinHeap();
    leftchild = BinHeap()
    rightchild = BinHeap()
    a.heapList = L
    size = a.currentSize = len(L)

    temp = L[:3]
    a.heapList = temp
    size = a.currentSize = len(temp)

    return L

aList = [4, 9, 8, 20, 15, 6, 0, 9, 12, 11]

b = BinHeap()

# b.buildMinHeap(aList)
maxheapified = b.buildMaxHeap(aList)

print(maxheapified)
# b.insert(7)
# print(b.heapList)
maxheapified[1] = 5
# print(maxheapified)
b.heapList = maxheapified
b.currentSize = len(maxheapified)
print(b.maxheapify(1))
