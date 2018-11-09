'''
project.py
Katie Naughton and Ella Edmonds

eval, with x predefined
def square(x):
    return x*x
    result=square(5)
print(square(5))
'''
import math

function=input("What function would you like to analyze? ")
x1=int(input("Where do you want your interval to start? "))
x2=int(input("Where do you want your interval to end? "))
step = float(input("What do you want the step to be? "))

print(function)

ycoordlist=[]
for r in range(x1, (x2+1)):
    x=r
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlist.append(y)
    
print(ycoordlist)



'''
interval1 = []

for i in range(x1,(x2+1)):
    #if i == x2:
        #interval1.append(i)
    #else:
    interval1.append(i+step)
        
print(interval1)

interval2= []

for i in range(x1,(x2+1)):
    #if i == x2:
        #interval2.append(i)
    #else:
    interval2.append(i-step)
print(interval2)

'''    
intervalnum=len(ycoordlist)
print(intervalnum)

derivlist=[]
for s in range(intervalnum):
    deriv  = ((ycoordlist[s]+0.1)-(ycoordlist[s]-0.1))/(2*0.1)
    derivlist.append(deriv)

print (derivlist)



    





    
    
