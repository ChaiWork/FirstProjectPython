#concession stand program

#dictionary {key:value}

from ast import While


menu = {"Pizza": 3.00 ,
        "Nachos" : 4.50,
        "Popcorn" : 6.00,
        "Fries" : 2.50,
        "Chips" : 1.00,
        "Prezel" : 3.50,
        "soda" : 3.00,
        "lemonade":4.25}

cart= []
total=0

print("---------MENU-------------")

for key,value in menu.items():
    print(f"{key:10}: RM{value:.2f}")
    
print("--------------------------")

while True:
    food = input("Select an item(q to quit):")
    if food =="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
print("------------YOUR ORDER-------------")
        
for food in cart :
    total+=menu.get(food)
    print(food,end=" ")
    
print()
print(f"Total is : RM{total:.2f}")