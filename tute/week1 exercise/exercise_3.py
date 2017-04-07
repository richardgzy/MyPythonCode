# Q3

try:
    i = int(input("Please input a number to do factorial calculation:"))
    sum = 1
    for x in range(2, i + 1):
        sum = x * sum
    print("The factorial number is %d" % sum)
except Exception as e:
    print('Exception happened: ' + str(e))