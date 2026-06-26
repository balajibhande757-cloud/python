def div(a,b):
    try:

        c = a / b
        print(c)

    except Exception as e:
        print(e)

    # print("this is always executed") # for func this is not allowed



    finally:        # when we have func and want somnthin to print clearlythen finally
        print("this is always executed")


a = int(input("Enter num 1: "))
b = int(input("Enter num 2: "))
div(a,b)