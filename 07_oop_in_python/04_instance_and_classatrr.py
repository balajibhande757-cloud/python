class Employee:
    company="Asus"     # class atrribute

    def __init__(self,name,bond,salary,company):
        self.salary=salary    # create an instance attribute of name salary and assign with it salary                         
        self.bond=bond             #  niche bhi same
        self.name=name   
        self.company=company

    def get_info(self):
        print(f"name: {self.name}, for {self.bond} years for {self.salary}")

e1=Employee("lala", 3, 258300,"Tesla")
print(e1.company)   # will print instance attribute if present
print(Employee.company)
        


# OBJECT INTROSPECTION

print(dir(e1))
