def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-2)+fib(n-1)

print(fib(6))


def safe_divide(a, b):
    if b==0:
        return "cannot divide by 0"
    return a/b

print(safe_divide(4,0))