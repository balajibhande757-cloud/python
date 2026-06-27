class Employee:
    def __init__(self,salary):
        self._salary=salary

    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self,value):
        if (value<0):
            print("something went wrong")
        else:
            self._salary=value




e=Employee(3000000)
e.salary=8965

print(e.salary)