#static method = a method that belong to a class rather than any object from that class (instance) usually used for general utility functions 
# 
# 
# Intances methods = best for operations on instances of the class(objects) 
# static methods = best for utility functions that do not need acess to class data


class Employee:
    
    def __init__(self,name,position):
        self.name=name
        self.position = position
        
    def get_info(self):
        return f"{self.name}={self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_position =["Manager","Cashier","Cook","Janitor"]
        return position in valid_position
    
employee1 = Employee("Eugene","Manager")
employee2 = Employee("Squid","cashier")
employee3 = Employee("sponge","cook")
    
print(Employee.is_valid_position("Cook"))
print(employee1.get_info())