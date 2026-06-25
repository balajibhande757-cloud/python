# Class is a blueprint or a template   Eg form for containing data like name,age, etc

# Object= IT IS A SPECIFIC INSTANCE CREATED BY TEMPLATE I.E.(CLASS)
# eg for containing the data of lala doe

class Employee:
    company="HP"

    def get_salary(self):   # self is a way to refrence to the object of the class that would be created
        print(self)
        return 34522
    
e=Employee()           # an object of class employee is created here
print(e.get_salary())         # the employee e's  get_salary meathod called

e2=Employee()
print(e2.get_salary())
print(e2.company)



class Dog:  # We define a class called "Dog"
    species = "Canis familiaris" # A class attribute (shared by all Dogs)

    def __init__(self, name, breed):  # The constructor (explained later)
        self.name = name     # An instance attribute to store the dog's name
        self.breed = breed   # An instance attribute to store the dog's breed

    def bark(self):          # A method (an action the dog can do)
        print(f"{self.name} says Woof!")

# Now, let's create some Dog objects:
my_dog = Dog("Buddy", "Golden Retriever")  # Creating an object called my_dog
another_dog = Dog("Lucy", "Labrador")     # Creating another object

# We can access their attributes:
print(my_dog.name)       # Output: Buddy
print(another_dog.breed)  # Output: Labrador

# And make them perform actions:
my_dog.bark()            # Output: Buddy says Woof!
print(Dog.species)       # Output: Canis familiaris