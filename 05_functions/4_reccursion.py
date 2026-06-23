''' fibonachi series 
series= 0,1,1,2,3,5,8,13
index = 0,1,2,3,4,5,6.....
fib0=0
fib1=1
fib2=fib0+fib1
fib3=fib1+fib2
fib(n)=fib(n-2)+fib(n-1)


                  '''


def fib(n):
    if( n==0 or n==1):
        return n
    return fib(n-2)+fib(n-1)

print(fib(6))