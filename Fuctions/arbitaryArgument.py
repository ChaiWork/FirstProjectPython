#*args = allows you to pass multiple non-key arguments 
# **kwargs = allows you to pass multiple keyword-arguments 
# * unpacking operator

def add(*nums):
    total=0
    for num in nums:
        total+= num
    return total

print(add(1,2,3,4,5))

def display_name(*args):
    for arg in args:
        print(arg,end=" ")
        
display_name("DR","Spongebob", "Harold", "Squarepants","III")

def print_address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_address(street="Miharja",apt="100",city="Detroit",state="Sydney",zip="424654")