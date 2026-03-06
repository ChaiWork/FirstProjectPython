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


numbers = [1,-2,3,-4,5,-6,8]
positive_Numbers = [num for num in numbers if num>=0]
negative_Numbers = [num for num in numbers if num<=0]
even_nums = [num for num in numbers if num%2==0]
odd_Nums = [num for num in numbers if num%2==1]

print(positive_Numbers)
print(negative_Numbers)
print(even_nums)
print(odd_Nums)