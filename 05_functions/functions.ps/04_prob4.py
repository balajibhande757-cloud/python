def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial((n-1))

print(factorial(4))


def sum_of_digits(m):
    if m==0:
        return 0
    return m%10 + sum_of_digits(m//10)

print(sum_of_digits(7532))


# sum of digit 7532 is same as
#2(last digiit)+sum of digits 753