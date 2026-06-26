from functools import reduce
numbers=[1,2,5,8]
#       [3,5,8]
#       [8,8]
#       [16]
def sum(a,b):
    return a+b

c= reduce(sum,numbers)
print(c)