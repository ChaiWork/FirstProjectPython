def showBalance(balance):
    print("************************")
    print(f"Your Balance is RM{balance:.2f}")

def deposit():
    print("************************")
    amount = float(input("Enter an amount to be deposited"))
    
    if amount < 0:
        print("************************")
        print("Thats not a valid amount")
        return 0
        
    else:
        return amount


def withdraw(balance):
    print("************************")
    amount = float(input("Enter amount to be withdraw:"))
    
    if amount > balance:
        print("************************")
        print("Insufficient Funfs")
        return 0
    elif amount < 0:
        print("************************")
        print("Amount must be greater than 0")
        return 0 
    else:
        return amount 


def main():

        balance = 0
        is_running = True

        while is_running:
            print("************************")
            print("Banking Program")
            print("************************")
            print("1.Show Balance")
            print("2.Deposit")
            print("3.Withdraw")
            print("4.Exit")
            print("************************")
            
            choice = input("Enter your choice (1-4):")
            
            if choice=='1':
                showBalance(balance)
            elif choice=='2':
                balance+=deposit()
            elif choice == '3':
                 balance-= withdraw(balance)
            elif choice =='4':
                is_running= False
            else:
                print("************************")
                print("That is not valid choice")
                print("************************")
                
        print("************************")        
        print("Thank you have a Nice day")
        print("************************")
        
if __name__ =='__main__':        
        main()