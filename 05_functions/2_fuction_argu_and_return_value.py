# Positional Arguments

def add(a, b):        # a and b are parameters
    return a + b

c=add(3,4)         # passed values are arguments
print(c)


#default arguments

def greet(name="guest"):
    return (f"Hello {name} !")

print(greet())


# Keyword Arguments
def student(name,age):
    return(f"Name={name},Age={age}")
print(student(age=45,name="lala"))