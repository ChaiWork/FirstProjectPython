#List comprehension = A concise way to 
# create lists in python compact and easier
# to read than tradiotional loops [expression for
# value in iterable if condition]


import math


fruits = ["apple","orange","banana","coconut"]
fruit_chars= [fruit[0] for fruit in fruits]
print(fruit_chars)

doubles =[x*2 for x in range(1,11)]
triple=[y*3 for y in range(1,11)]
squares=[z*z for z in range(1,11)]

print(doubles)
print(triple)
print(squares)