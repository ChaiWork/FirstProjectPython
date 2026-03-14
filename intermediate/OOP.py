#OBJECT = a bundle of related attributes (variables) and methods (functiosn) 
# ex phone,cup,book you need a "class" to create many objects  
# 
# class =(blueprint) used to design the structure and layout of an project

from car import Car

        
car1=Car("Persona",2026,"red",False)
car2=Car("Ferrari",2021,"Blue",True)


print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)



print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car1.drive()
car2.stop()