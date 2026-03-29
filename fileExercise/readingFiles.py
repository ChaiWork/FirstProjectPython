# python reading files(txt,json,csv)
import json
import csv


#change file here
file_path="D:/codingProject/PythonProject/FirstProjectPython/fileExercise/input.csv"


#try:  (txt file read)
   # with open(file_path,"r") as file:
  #      content =file.read()
 #       print(content)
#except FileNotFoundError:
 #   print("That was not found")
#except PermissionError:
  #  print("You do not have permission to read that file")
    

#try:(json file read)
 #   with open(file_path,"r") as file:
   #     content =json.load(file)
    #    print(content)
#except FileNotFoundError:
 #   print("That was not found")
#except PermissionError:
 #   print("You do not have permission to read that file")
    
    
 #csv read   
try:
    with open(file_path,"r") as file:
        content =csv.reader(file)
        for line in content:
            print(line)
except FileNotFoundError:
    print("That was not found")
except PermissionError:
    print("You do not have permission to read that file")