# #READING FILE
# f = open("lala.txt", "r")
# content = f.read()
# print(content)
# f.close()


#WRITTING FILE
f=open("jon_doe.txt","w")

string='''jon doe is very briliant man and his favourite 
package is pandas'''


f.write(string)

# APPENDING FILE
f= open("jon_doe.txt","a")
string='''"\nhe lives in pakistan and he/she is transgender"'''
f.write(string)

#READ FILE LINE  BY LINE
f=open("jon_doe.txt","r")
for line in f:
    print(line)
f.close()