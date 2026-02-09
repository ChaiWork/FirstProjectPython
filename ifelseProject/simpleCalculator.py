

num1=int(input("Insert the first number :"))
num2=int(input("Insert the second number :"))
ope =input("WHAT IS THE OPERATION BETWEEN THIS 2 NUMBA (+,-,/,*): ")
result=0




if ope == "+":
        print("PLUS")
        result=num1+num2
        print(f"the result of plus is : {result}")
elif ope == "-":
        print("MINUS")
        result=num1-num2
        print(f"the result of plus is : {result}")
elif ope == "/":
        print("DIVIDE")
        result=num1/num2
        print(f"the result of plus is : {result}")
elif ope == "*":
        print("DARAB")
        result=num1*num2
        print(f"the result of plus is : {result}")
        
else:
    print("wrong operation")
