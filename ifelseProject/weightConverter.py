print("Choice 1 KG TO POUND ")
print("Choice 2 POUND TO KG ")
choic=input("Enter your choice")
result=0


if choic=='1':
    
    weightKg = float(input("Enter you Kg to convert in pound"))
    
    result=weightKg*2.20462262
    
    print(round(result,3))
    
elif choic=='2':
    weightPound=float(input("Enter you Pound to convert in Kg"))
    
    result= weightPound/2.20462262
    
    print(round(result,3))