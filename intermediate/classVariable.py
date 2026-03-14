#class variable = shared among all instances of a class defined 
# outside the constructor allow you to share data among 
# all objects treated from that class

class Student:
    
    class_year = 2024
    num_students = 0
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_students+=1
        
student1= Student("Ahmad", 20)
student2=Student("Siti", 14)
student3=Student("YUti", 11)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")

print(student1.name)
print(student2.name)
print(student3.name)