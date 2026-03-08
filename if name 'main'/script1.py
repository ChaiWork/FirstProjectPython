# if __name__ == __main__: (this script can imported or runn stanalone)
# fucntions and classes in this module can be reused wihout the main 
# block of code executing   good practicing (code is modular, helps readability, 
# leaves no global variable,avoid unintended execution)
# Ex. library = import library for functionality when running library directly, display a help page

#def main():
   # pass

#if __name__ == '__main__':
 #   main()
 
def favorite_food(food):
     print(f"Your favorite food is {food}")
     
def main():
    print("This is script1")
    favorite_food("Pizza")
    print("Goodbye")

if __name__ == '__main__':
    main()
     
     