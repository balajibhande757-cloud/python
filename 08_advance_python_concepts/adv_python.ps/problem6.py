p=[1, 2, 3, 4, 5]
cube=lambda x:x**3
l=list(map(cube,p))
print(l)


a=[10, 11, 12, 13, 14]
even= lambda x:x%2==0
l2=list(filter(even,a))
print(l2)


from functools import reduce
k=[1, 2, 3, 4]

product= lambda x,y:x*y
print(reduce(product,k))
