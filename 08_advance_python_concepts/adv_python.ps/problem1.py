# def decorator(func):
#     def wrapper():
#         print("can i execute hello")
#         func()
#         print("i execute succesfully")
#     return wrapper
    
# @decorator
# def lala():
#     print("Hello!")
# lala()



def logger(func):
    def wrapper():
        print("the function will be executed")
        func()
    return wrapper
@logger
def say_hello():
    print("Hello!")
say_hello()


from time import time
def timer(func):
    def wrapper(n):
        t1=time()
        func(n)
        t2=time()
        print(f"the time {t2-t1}")
        return f"the value {func(n)}"
    return wrapper
@timer
def sum_1m(n):
    sum=0
    for i in range (1,n+1):
        sum+=i
    return sum

a=sum_1m(1000000)
print(a)
