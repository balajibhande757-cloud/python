a=int(input("Enter a numer:"))
match(a):
    case 1:
        print("monday")
 
    case 2:
        print("tuesday")
 
    case 3:
        print("wednsday")
 
    case 4:
        print("thuesday")
 
    case 5:
        print("friday")
 
    case 6:
        print("saturday")
 
    case 7:
        print("sunday")
    case _:
        print("invalid")


num1=int(input("Enter first numer:"))
num2=int(input("Enter second numer:"))
operations=input("enter the opration you want")

match operations:
    case"+":
        print(num1+num2)
    case"-":
        print(num1-num2)
    case"*":
        print(num1*num2)
    case"/":
        print(num1/num2)
    case _:
        print("invalid")