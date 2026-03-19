#ducktyping = another way to achieve polymorphism besides inheritance 
# object must have the minimum neccassry attributes/methods if it looks 
# like a duck and quaks like a duck,it must me duck

class Animal:
    alive =True
    
class Dog(Animal):
    def speak(self):
        print("WOOF")
        
class Cat(Animal):
    def speak(self):
        print("MEOW")
        
class Car:# not in animal class or parent animal
    alive=False
    def speak(self):
        print("HONK")
        
        
animals =[Dog(),Cat(),Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)