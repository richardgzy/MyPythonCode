class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None
        self.height = 0
        self.leftChildHeight = 0
        self.rightChildHeight = 0

    def insertLeft(self, tree):
        assert self.leftChild is None
        self.leftChild = tree

    def insertRight(self, tree):
        assert self.rightChild is None
        self.rightChild = tree

    def preorderPrint(self):
        print(self.key)
        if self.leftChild is not None:
            self.leftChild.preorderPrint()
        if self.rightChild is not None:
            self.rightChild.preorderPrint()

    def inorderPrint(self):
        if self.leftChild is not None:
            self.leftChild.inorderPrint()
            print(self.key)
        if self.rightChild is not None:
            self.rightChild.inorderPrint()

    def postorderPrint(self):
        if self.leftChild is not None:
            self.leftChild.postorderPrint()
        if self.rightChild is not None:
            self.rightChild.postorderPrint()
            print(self.key)

    def measureHeight(self):

        if self.leftChild is not None:
            self.leftChildHeight = 1 + self.leftChild.measureHeight()
        elif self.rightChild is not None:
            self.rightChildHeight = 1 + self.rightChild.measureHeight()
        else:
            self.height = 0
            self.leftChildHeight = 0
            self.rightChildHeight = 0

        self.height = max(self.leftChildHeight, self.rightChildHeight)

        return self.height

    def findValueAtMinimumDepth(self, v):

        if self.key == v:
            return self.height

        elif self.leftChild is not None:
            if self.leftChild == v:
                return 1
            self.leftChildHeight = 1 + self.leftChild.findValueAtMinimumDepth(v)

        elif self.rightChild is not None:
            if self.rightChild == v:
                return 1
            self.rightChildHeight = 1 + self.rightChild.findValueAtMinimumDepth(v)

        else:
            self.height = 0
            self.leftChildHeight = 0
            self.rightChildHeight = 0

        self.height = max(self.leftChildHeight, self.rightChildHeight)

        return self.height

T1 = BinaryTree(7)
T1.insertLeft(BinaryTree(8))
T1.insertRight(BinaryTree(7))
T1.leftChild.insertLeft(BinaryTree(12))
T1.leftChild.insertRight(BinaryTree(9))
T1.leftChild.leftChild.insertLeft(BinaryTree(5))
T1.leftChild.leftChild.insertRight(BinaryTree(10))
T1.rightChild.insertLeft(BinaryTree(5))
T1.rightChild.insertRight(BinaryTree(6))


# newTree.preorderPrint()
# print(T1.measureHeight())
print(T1.findValueAtMinimumDepth(5))