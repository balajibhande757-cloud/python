def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator
        
@repeat(5)
def say_hello(a):
    print(f"Hello {a} !")


'''
 IT REPLACES THE FUNCTION SAY_HELLO 
def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
'''

'''
for i in range(5):             # this how it it acctually mean it
    say_hello("mahesh")'''

say_hello("mahesh")