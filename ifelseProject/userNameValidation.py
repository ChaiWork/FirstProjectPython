username =input("Enter your username : ")

if len(username)>12:
    print("Your username cant be more than 12 characters")
elif not username.find(" ")== -1:
    print("Your username cant contain spaces")
elif not username.isalpha():
    print("your username cant contain numbers")
else:
    print(f"Welcome{username}")