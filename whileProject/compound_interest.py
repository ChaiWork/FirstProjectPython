principle =0 
rate=0
time=0

while True:
    principle = float(input("Enter the principle Amount : "))
    if principle <0:
        print("principle cant be less than zero")
    else:
        break
    
while True:
    rate = float(input("Enter the interest Rate : "))
    if rate <0:
        print("interest rate cant be less than zero")
    else:
        break
    
while True:
    time = int(input("Enter the time taken : "))
    if time <0:
        print("time taken  cant be less than zero")
    else:
        break
    
amount = principle* pow((1 +rate/100),time)
print(f"Balance after {time} year/s : ${amount:.2f}")