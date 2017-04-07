'''
Created on Feb 2, 2017

@author: Richard's Surface
'''
def power(x,n):
    value = 1
    if n > 0:
        value = power(x, n//2)
        if n % 2 == 0:
            value = value * value
        else:
            value = value * value * x
            
    return value;
print(power(2,3));
print(2**3)

# stack = [2,3,5,6,9];
# while stack != []:
#     print(stack.pop());
# print(stack[0])