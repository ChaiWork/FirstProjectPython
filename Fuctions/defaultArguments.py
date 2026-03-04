#default arguments = a default value for parameters defaut is used 
# when that argument is omitted make your
# fuctios more flexible 

import time

def count(end,start=0):
    for x in range (start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")
    
count(30,1)