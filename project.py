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
step = float(input("what do you want the step to be? "))


print(function)

'''
x=xin

def ycoord(xin):
    return eval(function)
    result=ycoord(xin)
 

ycoordlist=[]
for r in range(x1, (x2+1)):
    ycoordlist.append(result(r))
    
print(ycoordlist)
''' 

#func = function(equation)

interval1 = []

for i in range(x1,(x2+1)):
    if i == x2:
        interval1.append(i)
    else:
        interval1.append(i+step)
        
print(interval1)

interval2= []

for i in range(x1,(x2+1)):
    if i == x2:
        interval2.append(i)
    else:
        interval2.append(i-step)
print(interval2)
    
steplist=len(interval1)
print(steplist)


derivlist=[]
for s in range(steplist):
    deriv  = (interval1[s]-interval2[s])/(2*step)
    derivlist.append(deriv)

print (derivlist)



    





    
    
