#python writing files (.txt , .json ,.csv)

import json
import csv


txt_data = "I like KFC"


#ubah file path
file_path="D:/codingProject/PythonProject/FirstProjectPython/fileExercise/output.csv"

#txt
employees= ["Euguene","Sqauidward","Spongebob","Sandy"]

#json
employee2 = {"name":"Spongebob",
             "age":30,
             "job":"cook"
             }   #dictionary KEYWORD/ JSON DATA



#csv
employeees1= [["Name", "Age","Job"],
             ["Spongbob",30,"Cook"],
             ["Patrick",29,"Unemployed"],
             ["sandy",25,"Scientist"]]



#try: (CREATE FILE)
 #   with open(file_path,"x") as file:
  #      file.write(txt_data)
   #     print(f"txt file {file_path} was created")
#except FileExistsError:
#    print("That file already exist")

#try: (APPEND FILE)
 #   with open(file_path,"a") as file:
  #      file.write("\n" + txt_data)
   #     print(f"txt file {file_path} was created")
#except FileExistsError:
 #   print("That file already exist")
    
#try: (WRITE EVERY EMPLOYEE )
 #   with open(file_path,"w") as file:
  #       for employee in employees:
   #         file.write(employee + "\n")
    #        print(f"txt file {file_path} was created")
#except FileExistsError:
 #   print("That file already exist")
 
#try: (DICTIONARY KEYWORD)
 #   with open(file_path,"w") as file:
  #      json.dump(employee2,file,indent=4)
   #     print(f"json file {file_path} was created")
#except FileExistsError:
 #   print("That file already exist")
 
try: 
  with open(file_path,"w",newline = "") as file:
        writer = csv.writer(file)
        for row in employeees1:
            writer.writerow(row)
        print(f"csv file {file_path} was created")
except FileExistsError:
       print("That file already exist")