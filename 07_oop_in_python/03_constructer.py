class Employee:
    def __init__(self,name,bond,salary):
        self.name=name
        self.bond=bond
        self.salary=salary

    def get_info(self):
        print(f"name of the employee {self.name},the bond with company for {self.bond} years for {self.salary} salary")

e=Employee("lala",2,225000)
print(e.get_info())