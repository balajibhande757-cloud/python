def sum_all(*args):
    sum=0
    for item in args:
        sum+=item
    return sum
    

print(sum_all(8,55,6))




def print_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_details(name="Alice", age=25, city="Delhi")