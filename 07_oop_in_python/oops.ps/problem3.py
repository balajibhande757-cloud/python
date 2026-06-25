class Animal:
    def sound(self):
        print("some sound")
class Dog(Animal):
    def sound(self):
        print("Bark!")


a=Animal()
a.sound()

b=Dog()
b.sound()