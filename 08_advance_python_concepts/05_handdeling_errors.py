while True:
    try:
        a= int(input("Enter num 1:"))
        b= int(input("Enter num 2:"))
        print(f"the division is {a/b}")
    except ValueError:
        print("hey do do wrong typecast")
    except ZeroDivisionError:
        print("dont divide by zero")
    except Exception as e:
        print("something went wrong!",e)