def sum(x,y):
    # x and y are the local variable
    c=x+y
    z=1        # it creates local variable it is in sum function
    return c
z=8   # it is global variable
print(sum(4,5))
print(z)



#  GLOBAL KEYWORD
def sun(a,b):
    print("hi i am lala")
    c=a+b
    global z # please modify global z
    z=0
    return c
z=78          #global
print(sun(4,8))
print(z)