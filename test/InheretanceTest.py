class Animal:

    def __init__(self, head, foot):
        self.head = head
        self.foot = foot

    def makesound(self):
        print("my head is %s and my foot is %s" % (self.head, self.foot))
        return

class Cat(Animal):

    def __init__(self, head, foot, escape):
        Animal.__init__(self, head, foot)
        self.escape = escape

    def catshow(self):
        print("Meow, cat escape %s" % self.escape)

# ani = Animal("head", "foot")

c = Cat("head", "foot", "school")
c.makesound()
c.catshow()