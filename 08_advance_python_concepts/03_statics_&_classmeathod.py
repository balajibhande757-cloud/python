class Employee:
    company="HP"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    # INSTANCE MEATHOd
    def print_info(self):
        print(f"the name {self.name} and salary is {self.salary}")
    
    #STATIC MEATHOD
    @staticmethod
    def sum(a,b):
        return a+b
    
    #CLASS MEATHOD
    @classmethod
    def print_company(cls):
        print(cls.company)
    
    @classmethod
    def changet_company(cls,new_company):
        cls.company=new_company
    



e1=Employee("jack Doe",58218)
e2=Employee("doggy don",822588)
print(Employee.company)   
# e1.print_company()     # by classmeathod for refrencing classargument
e1.changet_company("Acer")
# e1.print_company()     # by classmeathod for refrencing classargument
print(Employee.company)
# e1.print_info()
# print(e2.sum(2,6))