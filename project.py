'''
project.py
Katie Naughton and Ella Edmonds
'''
import math
function=input("What function would you like to analyze? ")
a=int(input("Where do you want your interval to start? "))
b=int(input("Where do you want your interval to end? "))

print(function)
funclist=list(function)
print(funclist)

length=len(funclist)
print(length)

lamda=lambda x:
ycoordlist = []
for x in funclist:
    ycoordlist.append(x)
print(ycoordlist)
    
output=""
for y in ycoordlist:
    output += y + " "
print(output)

for r in range (a, (b+1)):
    ycoord=lambda x: output
    print(ycoord(x))
    
#for r in c
'''
ycoord=[]
for x in range(a, (b+1)):
    print (function)

#linearization= lamba a: f(a)+ fp(a)(x-a)
#for x in range(a,(b+1)):
'''
    
    
