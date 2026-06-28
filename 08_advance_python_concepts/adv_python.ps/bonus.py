# while True:
#     class invalid_inp(Exception):
#         pass
#     try:
#         a=int(input("Enter first no:"))
#         b=int(input("Enter second no:"))
#         def div_of(a,b):
#             if(b==0):
#                 raise invalid_inp("Error ur input is invalid")
#             else:
#                 print(a/b)
#         div_of(a,b)

#     except invalid_inp as e:
#         print(e)
        

# def decorator(func):
#     def wrapper(*args,**kwargs):
#         print("before")
#         res=func(*args,**kwargs)
#         print("after")
#         return res

#     return wrapper

# @decorator
# def add(a,b):
#     return a+b

# @decorator
# def intro(name,age):
#     print(f"my name is {name} and age {age}")

# print(add(6,2))
# intro("lala",34)


class vector:
    def __init__(self, x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        return(self.x+other.x,self.y+other.y)

    def __str__(self):
        return f"{self.x} {self.y} "
e=vector(9,4)
e1=vector(7,5)
v = e.__add__(e1)
print(v)