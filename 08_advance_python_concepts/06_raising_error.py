# a= int(input("Enter num 1:"))
# b= int(input("Enter num 2:"))
# if b==0:
#     raise ValueError("pls dont divide by zero")
# print(f"the division is {a/b}")

try:
    a=45/0
    a=45/10

except Exception as e:
    print(e)

#GETS EXECUTE WHEN THERE IS NO ERROR IN TRY BLOCK
else:
    print("hey i am good") 
