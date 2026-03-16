#inheritance = allow a class to inherit attributes and methods from another class
# helps with code resusability and extensibility class Child(Parent)


class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping")
        
class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

class  Mouse(Animal):
    def speak(self):
        print("squeek")


dog = Dog("Sccoby")
cat = Cat("Tom")
mouse = Mouse("Jerry")

print(dog.name,dog.is_alive)

dog.eat()
dog.sleep()