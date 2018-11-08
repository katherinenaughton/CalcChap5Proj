'''
project.py
Katie Naughton and Ella Edmonds
'''
#eval, with x predefined

#def square(x):
    #return x*x
    #result=square(5)
import math
function=input("What function would you like to analyze? ")
a=int(input("Where do you want your interval to start? "))
b=int(input("Where do you want your interval to end? "))

print(function)

def ycoord(x):
    return eval(function)
    result=ycooord(5)

ycoordlist=[]
for x in range(a, (b+1)):
    result=ycoord(x)
    ycoordlist.append(result)
    
print(ycoordlist)


    





    
    
