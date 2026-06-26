class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @property
    def first_name(self):
        l= self.name.split(" ")
        return l[0]
    @first_name.setter
    def first_name(self,first):
        l= self.name.split(" ")
        new_name=f"{first},{l[1]}"
        self.name=new_name
   


e1=Employee("jack Doe",58218)
e2=Employee("doggy don",822588)



# print(e1.name)
print(e1.first_name)
e1.first_name="lala+"
print(e1.name)


# e1.set_last_name("khan")
# e2.set_first_name("lala")
# print(e2.name)
# print(e1.name)