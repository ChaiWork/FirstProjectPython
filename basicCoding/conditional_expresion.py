#conditional expression = a one-line shortcut if else operator
# print or assign  one of two values based on a conditon
# X if condition else Y


  
user_role="guest"

access_level = "Full access" if user_role=="admin" else "limited access"

print(access_level)