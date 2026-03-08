from script1 import*

def favorite_drink(drink):
    print(f"Your favorite drink is {drink}")
    
def main():    
    print("this is script2")
    favorite_food("susshi")
    favorite_drink("Milo")
    print("Goodbye")

if __name__ == '__main__':
    main()