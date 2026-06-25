class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print_person(self):
        print(f"name is {self.name} and {self.age} years old")

p1=person("jon Doe",23)
# print(p1.name,p1.age)
p1.print_person()