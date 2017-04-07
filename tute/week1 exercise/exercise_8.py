# Q8

class library:

    def readfile(self):
        file = open("exercise_8.dat")
        try:
            data = file.read()
            booklist = data.split(" - ")
            for i in range(0, len(booklist)):
                newbook = book(booklist[i], True)
                booklist[i] = newbook
            return booklist
        except Exception as e:
            print(str(e))
        finally:
            file.close()

    def display(self,booklist):
        for i in range(0, len(booklist)):
            print(i + 1, ".", booklist[i].getname())

    def printmenu(self):
        print("Welcome to my library:")
        print("1.display")
        print("2.check ID")
        print("3.borrow ID")
        print("4.return ID")
        print("5.quit library")
        print("")

    def checkID(self, book):
        if book.available:
            print("This book is ready for borrowing")
        else:
            print("This book has been borrowed")

    def borrowID(self, book):
        if not book.available:
            return "This book has already been borrowed,operation failed"
        else:
            book.available = False
            return "Operation succeed"

    def returnID(self, book):
        if book.available:
            return "This book is already free for borrowing"
        else:
            book.available = True
            return "Operation succeed"

    def run(self):
        booklist = self.readfile()
        self.printmenu()
        choice = int(input("Please choose:"))
        while choice != 5:
            # self.printmenu()
            if choice in (2, 3, 4):
                searchid = int(input("Please enter a book ID(positive integer):"))
                searchbook = booklist[searchid - 1]
                dict1 = {2: self.checkID(searchbook), 3: self.borrowID(searchbook), 4: self.returnID(searchbook)}
                dict1.get(choice)
                self.printmenu()
            elif choice in (1, 5):
                dict2 = {1: self.display(booklist), 5:exit(0)}
                dict2.get(choice)
                self.printmenu()
            else:
                print("Invalid Input")

class book:

    def __init__(self, name, available):
        self.name = name
        self.available = available

    def getname(self):
        return self.name

    def getavailable(self):
        return self.available


newlibrary = library()
newlibrary.run()