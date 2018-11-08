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
a=int(input("Where do you want your interval to start? "))
b=int(input("Where do you want your interval to end? "))

x=x2

print(function)

def ycoord(x2):
    return eval(function)
    result=ycoord(x2)
 

ycoordlist=[]
for x in range(a, (b+1)):
    
    ycoordlist.append(result(x))
    
print(ycoordlist)

equation = input("what equation would you like me to analize")
x1 = int(input("on what interval? start value:"))
x2 = int(input("on what interval? end value:"))
step = input("what do you want the step to be")

#func = function(equation)

interval = []

for i in range(x1,x2+1):
    if i == x2:
        interval.append(i+.0)
    else:
        for m in [.0,.1,.2,.3,.4,.5,.6,.7,.8,.9]:
            #print(i+m)
            interval.append(i+m)

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


    





    
    
