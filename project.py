'''
project.py
Katie Naughton and Ella Edmonds
'''
import math
func1=input("What function would you like to analyze? ")
a=int(input("Where do you want your interval to start? "))
b=int(input("Where do you want your interval to end? "))

print(func1)
funclist=list(func1)
print(func1)

length=len(funclist)
print(length)

ycoord = lambda x: func1
for x in range(a, (b+1)): 
    print(ycoord(x))

#for r in c
'''
ycoord=[]
for x in range(a, (b+1)):
    print (function)

#linearization= lamba a: f(a)+ fp(a)(x-a)
#for x in range(a,(b+1)):
'''
    
    
