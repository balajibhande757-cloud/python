class neg_no_error(Exception):
    pass
        
try:
    num=int(input("Enter a number:"))
    if num<0:
        raise neg_no_error(" Error:the value is negative")
    result=45/num
    print(f"the result is {result}")
        

except ValueError:
    print("Error: please enter proper no")

except ZeroDivisionError:
    print("Error: division by zero")

except neg_no_error as e:
    print(e)