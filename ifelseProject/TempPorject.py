unit = input("What is Unit temparature is it in C (Celcius) or in F (Fahrenheit)")
Temp = float(input("WHat is the temparature"))
if unit == 'C':
    Temp =round((9*Temp)/5+32,1)
    print(f"the temparature  in fahrenheit is : {Temp}F")
elif unit == 'F':
    Temp =round((Temp-32)*5/9,1)
    print(f"the temparature  in fahrenheit is : {Temp}C")
else:
    print("Wrong unit")