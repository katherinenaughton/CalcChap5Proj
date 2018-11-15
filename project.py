'''
project.py
Katie Naughton and Ella Edmonds

TO DO: 
have figure out how to tell if extrema is abs/local or max/min
have to figure our when decreasing or increasing interval is a union
deals with logs 1/x graphs
'''

                                            #This is where we import the functions from the math library. 
from math import sin, cos, tan, acos, asin, atan
from math import exp, expm1, e, pi
from math import log, log10, sqrt, log2
from ggame import App, Color, LineStyle, Sprite
from ggame import CircleAsset

                                            #This is where the user inputs the function and intervals. 
function=input("What function would you like to analyze? ")

x1=int(input("Where do you want your interval to start? Remember that your interval must be within the domain of the function:) "))
x2=int(input("Where do you want your interval to end? Remember that your interval must be within the domain of the function:)"))

'''
try:
    print(code with error)
except:
    print (you messed up)
'''
        


#print(function)

xcoordlist=[]                               #This prints a list of the x values. 
for i in range(x1,x2+1):
    if i == x2:
        xcoordlist.append(i+.0)
    else:
        for m in [.0,.1,.2,.3,.4,.5,.6,.7,.8,.9]:
            #print(i+m)
            xcoordlist.append(i+m)
#print(xcoordlist)
    

ycoordlist=[]                               #This prints a list of the y values. 
for r in xcoordlist:
    x=r
    Locfunction=function.lower()
    try:
        y=eval(Locfunction)
        ycoordlist.append(y)
    except: 
        print("There is an asymptote in this function!")

#print(ycoordlist)

                                             #This will find the y+.001 value for the symmetric difference quotient.
ycoordlist1=[]                              
for r in xcoordlist:
    x=r+0.001
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlist1.append(y)
#print(ycoordlist1)


ycoordlist2=[]                              #This will find the y-.001 value for the symmetric differnce quotient. 
for r in xcoordlist:
    x=r-0.001
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlist2.append(y)
#print(ycoordlist2)


intervalnum=len(ycoordlist1)                #This tells us how long our cordinate lists are 
#print(intervalnum)                            #so we know how long to run the loop. 


derivlist=[]                                #This makes a list of the derivatives, and a rounded list
derivlist1=[]                                   #of the derivatives. 
for s in range(intervalnum):
    deriv  = ((ycoordlist1[s])-(ycoordlist2[s]))/(2*0.001)
    derivlist1.append(round(deriv,2))
    derivlist.append(deriv)
#print (derivlist1)

                                            #This makes a list of the x and y coordinates, and the list of 
#deriv/x value/y value zip                      #corresponding derivatives. 
xyderivzip=list(zip(xcoordlist, ycoordlist, derivlist1))
#print(xyderivzip)


extremalist=[]                              #This finds where the derivative equals zero, and also
increasinglist=[]                           #where the function is increasing and decreasing. 
decreasinglist=[]
for d in xyderivzip:
    if d[2]==0:
        extremalist.append((d[0], d[1]))
    if d[2]>=0:
        increasinglist.append(d[0])
    elif d[2]<=0:
        decreasinglist.append(d[0]) 
#print ('the first derivative of your equation is equal to zero at:',extremalist)
lengthincreasing=len(increasinglist)
lengthdecreasing=len(decreasinglist)

#if lengthdecreasing == 0:
    #print('Your function is never decreasing')
#else:
    #print('Your function is decreasing from',decreasinglist[0],'to',decreasinglist[-1])
    
#if lengthincreasing == 0:
    #print('Your function is never increasing')
#else:
    #print('Your function is increasing from',increasinglist[0],'to',increasinglist[-1])
 
#work on the print statements above to make it work when it changes from increasing to decreasing more than once

                                                    # This creates list of the y+0.001 and y-0.001 values to use
                                                        # in the symmetric differnce quotient to find the 
                                                            #second derivatives. 
#second derivatives
y2coordlist1=[]
for d in derivlist:
    y2coordlist1.append(d+0.001)
    
y2coordlist2=[]
for d in derivlist:
    y2coordlist2.append(d-0.001)

interval2num=len(y2coordlist1)
#print(interval2num)
                                                    #This creates a list of the rounded second derivatives.
deriv2list=[]
for i in range(interval2num):
    deriv2  = ((y2coordlist1[i])-(y2coordlist2[i]))/(2*0.001)
    deriv2list.append(round(deriv2,2))
#print (deriv2list)
                                                    #This creates a list with the x and y coordinates, 
                                                        #first derivatives and second derivatives. 
xyderiv2zip=list(zip(xcoordlist, ycoordlist, derivlist, deriv2list))
#print(xyderiv2zip)

                                                    #These loops check to see where the second derivative is zero,
                                                        #positive or negative in order to determine POI and concave
                                                            #up and down intervals. 
# points of inflection
poilist=[]
concaveuplist=[]
concavedownlist=[]
for d in xyderiv2zip:
    if d[3]==0:
       poistlist.append((d[0], d[1]))
    elif d[3]>=0:
        concaveuplist.append(d[0])
    elif d[3]<=0:
        concavedownlist.append(d[0])
#print (poilist)
#print (concaveuplist)
#print (concavedownlist)

# concave up interval(s)
concaveuplist=[]
for d in xyderiv2zip:
    if d[3]>=0:
        concaveuplist.append(d[0])
#print (concaveuplist)
lengthconcaveup=len(concaveuplist)
#print(lengthconcaveup)
#print('Your function is concave up from' concaveuplist[0] 'to' concaveuplist[-1])

#concave down interval(s)
concavedownlist=[]
for d in xyderiv2zip:
    if d[3]<=0:
        concavedownlist.append(d[0])
#print (concavedownlist)
lengthconcavedown=len(concavedownlist)
#print('Your function is concavedown from' concavedownlist[0] 'to' concavedownlist[-1])

                                    #This is the code for the graphs of the function and derivative.
                                    #This defines the colors.
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
purple = Color(0x800080, 1.0)
purple2 = Color(0x9932CC, 1.0)
                                    #This defines the points that will plot the function graph.
thinline = LineStyle(1, black)
points = CircleAsset(5, thinline, blue)
                                    #This defines the coordinates to graph the original function. 
graphycoords=[y*-1 for y in ycoordlist]
print(graphycoords)
xcoords = xcoordlist
ycoords= graphycoords

#print(xcoordlist)
#print(ycoordlist)
                                    #This graphs the function. 
xycoords=list(zip(xcoords,ycoords))
for i in xycoords: 
    Sprite(points, ((25*(i[0]+20),(25*(i[1]+10)))))

                                    #This defines the points that will plot the graph.
points = CircleAsset(5, thinline, purple)
                                     #This defines the coordinates to graph the derivative.
graphy2coords=[y*-1 for y in derivlist]
x2coords = xcoordlist
y2coords = graphy2coords
xy2coords=list(zip(x2coords,y2coords))
                                     #This graphs the derivative.
for i in xy2coords: 
    Sprite(points, ((25*(i[0]+20)),(25*(i[1]+10))))

myapp = App()
myapp.run()


    
    