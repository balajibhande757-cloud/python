#(parents class)
class Animal:
    location ="austraelia"
    def __init__(self,name):
        self.name=name
    
    def speak(self):
        print("speaking now....")
        #(child class)
class dog(Animal):     # this is how inheritance work  in python
    def speak(self):
        super().speak()     # we are ussing the speak function of parent class
        print("Woof!")
    
# a=Animal("Dog")

d=dog("Bruno")
d.speak()
print(d.location)


