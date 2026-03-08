#variable scope = where a variable is visible and 
# accessible sope resolution = (LEGB) Local -> 
# Enclosed -> Global -> Built in

#local 
def func1():
    x = 1
    print(x)
    
def func2():
    x = 2 
    print(x)
    
func1()
func2()


#enclose 
def func3():
    x = 1
    def func4():
        x = 2 
        print(x)
    func2()
    
func3()

#global
def func5():
    print(x)
    
def func6():
    print(x)
    
x=3
func5()
func6()

#built_in

from math import e
def funMath():
    print(e)
    


funMath()