def decorator(func):  # it is a fun that take the func which creates a new fun inside its body 
    # an after creating new  it return that new fun
    def wrapper():
        print("i will execute the hello.....")
        func()
        print("i succesfully executed the hello")
    return wrapper

@decorator
def say_hello():
    print("Hello!")


say_hello()          # if i want say_hello will execute the @decorator is imp in this case


# f=decorator(say_hello)       #f is new  created function
# f()

'''def f():
        print("i will execute the hello.....")
        print("Hello!")                           # and this how  f function looks
        print("i succesfully executed the hello")'''