# super()= function used in child class to call methods from a parent class(Superclass)
# Allows you to extend the functionality of the inheritance method



class Shape:
    def __init__(self,color,is_filled):
        self.color =color
        self.is_filled = is_filled
        
    def describe(self):
        print(f"It is {self.color} and {'Filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius=radius
        
    def describe(self):
        super().describe()
        print(f"It is a circle with an area of {3.14 * self.radius*self.radius}cm2")
        

class Square(Shape):
        def __init__(self,color,is_filled,witdh):
         super().__init__(color,is_filled)
         self.witdh=witdh
         
        def describe(self):
            super().describe()
            print(f"It is a Square with an area of { self.witdh*self.witdh}cm2")
        

class Triangle(Shape):
        def __init__(self,color,is_filled,witdh,height):
         super().__init__(color,is_filled)
         self.witdh=witdh
         self.height =height
         
        def describe(self):
            super().describe()
            print(f"It is a Triangle with an area of {self.witdh*self.height/2}cm2")
        
         
circle=Circle("Red",True,5)
square=Square("Yellow",True,10)
triangle=Triangle("Perang",True,10,5)

print(circle.color,circle.is_filled,)
print(f"{circle.radius}cm")


print(triangle.color)
print(triangle.is_filled)
print(triangle.witdh)
print(triangle.height)


circle.describe()
triangle.describe()
square.describe()