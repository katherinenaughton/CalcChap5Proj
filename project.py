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
        interval.append(i)
    else:
        interval.append(i+step)
        
print(interval)

interval2= []

'''f = []
part = []
for m in equation:
    if m != "+" or "-":
        part.append(m)
    elif m == "-" or m == ":
        f.append(part)
        part = []'''

f1  = lambda a: ((a+.01)-(a-.01))/(2*.01)

for m in interval:
    print(f1(m))


    





    
    
