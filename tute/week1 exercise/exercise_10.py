#Q10

# def weirdorials(n):
#     result = 0
#     if n <= 0:
#         result = 1
#     elif n >= 1 and n % 2 == 0:
#         result = weirdorials(n - 1) + n
#     elif n >= 1 and n % 2 == 1:
#         result = weirdorials(n - 1) * n
#     print(result)
#
# weirdorials(5)






#Test in lec

def isempty(l):
    return not l

def head(l):
    return l[0]

def tail(l):
    return l[1:]


# def length(l):
#     length = 0
#     while not isempty(l):
#         length += 1
#         l = tail(l)
#     return length

# def length2(l):
#     length = 0
#     if isempty(l):
#         return 0
#     else:
#         return 1 + length2(tail(l))


# def findrec(l, x):
#     if isempty(l):
#         return False
#     elif x == head(l):
#         return True
#     else:
#         return findrec(tail(l), x)
#
# def finditr(l, x):
#     for item in l:
#         if x == item:
#             return True
#     return False

# def total(l):
#     if isempty(l):
#         return 0
#     else:
#         return l[0] + total(tail(l))

# def maximun(l):
#     if isempty(l):
#         return None
#     else:
#         bestsofar = maximun(tail(l))
#         if bestsofar == None:
#             return head(l)
#         else:
#             return max(head(l), bestsofar)


def checknondecreasing(l):
    if isempty(l) or tail(l) == []:
        return True
    elif head(l) < tail(l)[0]:
        checknondecreasing(tail(l))
        return True
    else:
        return False


def checknondecreasing2(l, previous = None):
    if not l:
        return True
    else:
        current = head(l)
        if previous == None or previous <= current:
            return checknondecreasing2(tail(l), current)
        else:
            return False


# def splitint(x):
#     result = 0
#     if x in (0, 1):
#         result = 1
#         return result
#     else:
#         return 2 + splitint(x - 1)



#Test Area


l = [1, 2, 3, 4, 5]
s = [5, 4, 3, 0, 1]
empty = []
# print(length(l))

# print(length2(l))

print(checknondecreasing(s))
print(checknondecreasing2(s))

# print(splitint(100))