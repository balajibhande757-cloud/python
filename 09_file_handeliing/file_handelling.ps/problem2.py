# with open("tasks.txt","w") as f:
#     f.write("line1\n")
#     f.write("line2\n")
#     f.write("line3\n")

# with open("tasks.txt","a") as f:
#     f.write("the task is completed")
    
    
with open("tasks.txt","r") as f:
    for line in f.readlines():
        print(line)