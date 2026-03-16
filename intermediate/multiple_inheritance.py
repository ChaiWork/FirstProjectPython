# multiple inheritance = inherit from more than one parent class C(A,B)
# 
# multilevel inheritance = inherit from a parent which inherits from another parent C(B)<-B(A)<A


class Animal:
    
    def __init__(self,name):
        self.name=name
        
    def eat(self):
        print(f"{self.name} animal is eating")
        
    def sleep(self):
        print(f"{self.name} animal is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} animal is fleeing")
        
class Predator(Animal):
    def hunt(self):
        print(f"{self.name} animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass


hawk= Hawk("Tony")
fish= Fish("Nemo")


def display():
    rabbit =Rabbit("Bugs")
    rabbit.sleep()
    rabbit.eat()
    rabbit.flee()
    



display()