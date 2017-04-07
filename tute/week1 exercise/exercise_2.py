# #Q2

try:
    number = int(input("Please input a integer:"))
    if number % 2 != 0:
        print("%d is even" % number)
    elif number % 2 == 0:
        print("%d is odd" % number)
except Exception as e:
    print('Exception happened: ' + str(e))