from random import choice


while True:
    print("1 : Say hello")
    print("2 : Say goodbye")
    print("3 : Say quiting")
    
    choice = int(input("Please input the number"))
    
    if choice == 1:
        print("Hello!!")
    elif choice == 2:
        print("Goodbye")
    elif choice == 3:
        print("Quiting") 
        break
    else:
        print("invalid choice")