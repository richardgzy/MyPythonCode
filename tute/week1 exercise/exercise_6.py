# Q6

result = 1
try:
    n = int(input("Please input a positive integer:"))
    for i in range(0, n + 1):
        if i <= 0:
            result = 1
        elif i >= 1 and i % 2 == 0:
                result = result + i
        elif i >= 1 and i % 2 == 1:
                result = result * i
    print(result)
except Exception as e:
    print('Exception happened: ' + str(e))