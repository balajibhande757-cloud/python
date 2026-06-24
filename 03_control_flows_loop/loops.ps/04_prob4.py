sum=0
i=0
while i<=100:
    sum +=i
    i +=1
print(sum)


i=1
while i<11:
    print(i)
    i=i+1

password = "mahesh123"
entered_pass=input("Enter the password")
while (entered_pass != password):
    entered_pass=input("Wrong password! pls Enter the new password")
print("you are logged in ")


num =6454
print(int(str (num) [::-1]))