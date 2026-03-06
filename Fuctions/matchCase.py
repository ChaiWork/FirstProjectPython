# Match-case statement (Switch): an alternative to 
# using many "elif" statements execute 
# some code if  a value matches a 'case' 
# benefits:cleaner and syntax is more readeable


    
def is_weekend(day):
    match day:
        case "Saturday"|"Sunday":
            return True
        case "Monday"|"Tuesday"| "Wednesday"|"Thursday"|"Friday":
            return False
        case _ :
            return False
        
        
while True:
    user_Choice = input("Enter a Weekend or press Q to quit :")
    
    if user_Choice.upper()=="Q":
        
        print("Thank for using this program")
        break
    print(is_weekend(user_Choice)) 
    
    