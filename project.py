'''
project.py
Katie Naughton and Ella Edmonds

eval, with x predefined
def square(x):
    return x*x
    result=square(5)
print(square(5))

TO DO: 
have figure out how to tell if extrema is abs/local or max/min
have to figure our when decreasing or increasing interval is a union
MAKE THE DERIVATIVES OF O INTEGERS
'''
from math import sin,cos, tan, acos, asin, atan
from math import exp, expm1, e, pi
from math import log, log10, sqrt, log2

#inputs
function=input("What function would you like to analyze? ")
x1=int(input("Where do you want your interval to start? "))
x2=int(input("Where do you want your interval to end? "))
#step = float(input("What do you want the step to be? "))

#function
print(function)

xcoordlist=[]                               #x values
for i in range(x1,x2+1):
    if i == x2:
        xcoordlist.append(i+.0)
    else:
        for m in [.0,.1,.2,.3,.4,.5,.6,.7,.8,.9]:
            #print(i+m)
            xcoordlist.append(i+m)
#print(xcoordlist)
    
# y values
ycoordlist=[]
for r in range(x1, (x2+1)):
    x=r
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlist.append(y)
print(ycoordlist)

ycoordlist1=[]
for r in range(x1, (x2+1)):
    x=r+0.001
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlist1.append(y)
print(ycoordlist1)

ycoordlist2=[]
for r in range(x1, (x2+1)):
    x=r-0.001
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlist2.append(y)
print(ycoordlist2)

intervalnum=len(ycoordlist1)
print(intervalnum)

# derivatives
derivlist=[]                                #here we will make a list of the derivatives
derivlist1=[]
for s in range(intervalnum):
    deriv  = ((ycoordlist1[s])-(ycoordlist2[s]))/(2*0.01)
    derivlist1.append(round(deriv,2))
    derivlist.append(deriv)
print (derivlist1)

#deriv/x value/y value zip
xyderivzip=list(zip(xcoordlist, ycoordlist, derivlist1))
print(xyderivzip)

# extrema
extremalist=[]
for d in xyderivzip:
   if d[2]==0:
    extremalist.append((d[0], d[1]))
print (extremalist)

# increasing interval(s)
increasinglist=[]
for d in xyderivzip:
    if d[2]>=0:
        increasinglist.append(d[0])
print (increasinglist)

reverseincreasinglist=(increasinglist[::-1])
print(reverseincreasinglist)
print('Your function is increasing from', increasinglist[0], 'to', increasinglist[-1])

#decreasing interval(s)
decreasinglist=[]
for d in xyderivzip:
    if d[2]<=0:
        decreasinglist.append(d[0])
print (decreasinglist)

reversedecreasinglist=(decreasinglist[::-1])
print(reversedecreasinglist)
print('Your function is decreasing from', decreasinglist[0], 'to', decreasinglist[-1])

#second derivatives
y2coordlist1=[]
for d in derivlist:
    y2coordlist1.append(d+0.001)
    
y2coordlist2=[]
for d in derivlist:
    y2coordlist2.append(d-0.001)

interval2num=len(y2coordlist1)
print(interval2num)

deriv2list=[]
for i in range(interval2num):
    deriv2  = ((y2coordlist1[i])-(y2coordlist2[i]))/(2*0.001)
    deriv2list.append(deriv2)
print (deriv2list)

xyderiv2zip=list(zip(xcoordlist, ycoordlist, derivlist, deriv2list))
print(xyderiv2zip)

# points of inflection
poilist=[]
for d in xyderiv2zip:
   if d[3]==0:
    poistlist.append((d[0], d[1]))
print (poilist)

# concave up interval(s)
concaveuplist=[]
for d in xyderiv2zip:
    if d[3]>=0:
        concaveuplist.append(d[0])
print (concaveuplist)
lengthconcaveup=len(concaveuplist)
print(lengthconcaveup)
print('Your function is concave up from', concaveuplist[0], 'to', concaveuplist[-1])

#concave down interval(s)
concavedownlist=[]
for d in xyderiv2zip:
    if d[3]<=0:
        concavedownlist.append(d[0])
print (concavedownlist)
lengthconcavedown=len(concavedownlist)
print('Your function is concavedown from', concavedownlist[0], 'to', concavedownlist[-1])

    





    
    
