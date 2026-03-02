foods=[]
prices=[]
total=0

while True:
    food = (input("Please enter the food u want to buy or press q to quit : "))
    
    if food.lower() == "q":
        break
    else:
        price = float(input("Please enter the price of the food : "))
        foods.append(food)
        prices.append(price)
        
for food in foods :
    print(food,end=" ")
    
for price in prices :
    total+= price
    
print(f"Your total is : RM {total:.2f}")
        
