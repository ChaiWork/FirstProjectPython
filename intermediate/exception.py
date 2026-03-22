#exception = an event that interrupts the flow of a program (ZeroDivision,TypeError,ValueError)
#1. try 2.except 3finally


try:
    number =int(input("Enter a number:"))
    print(1/number)
except ZeroDivisionError:
    print("You cant divide by zero idiot")
except ValueError:
    print("Enter only number please!")
except Exception:
    print("Someting went wrong")
finally:
    print("Do some cleanyp here")