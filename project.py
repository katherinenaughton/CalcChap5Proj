
'''
project.py
Katie Naughton and Ella Edmonds
'''

                                            #This is where we import the functions from the math library. 
from math import sin, cos, tan, acos, asin, atan
from math import exp, expm1, e, pi
from math import log, log10, sqrt, log2
from ggame import App, Color, LineStyle, Sprite
from ggame import CircleAsset

                                            #This is where the user inputs the function and intervals. 
function=input("What function would you like to analyze? ")
print("If you choose a log function, make sure your interval is within the domain :)")
x1=int(input("Where do you want your interval to start (x value)? "))
x2=int(input("Where do you want your interval to end (x value)? "))

        
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


    
a=False
ycoordlist=[]                               #This prints a list of the y values. 
for r in xcoordlist:
    x=r
    Locfunction=function.lower()
    try:
        y=eval(Locfunction)
        ycoordlist.append(y)
    except: 
        a=True
        asymptote=r
        print("There is a vertical asymptote at x=", asymptote, " in this function!")
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
#print (derivlist)

                                            #This makes a list of the x and y coordinates, and the list of 
#deriv/x value/y value zip                      #corresponding derivatives. 
xyderivzip=list(zip(xcoordlist, ycoordlist, derivlist1))
#print(xyderivzip)

'''
extremalist=[]                              #here we find where d1 = 0
increasinglist=[]                           #here we find the interval where it inc/dec
decreasinglist=[]
zero = []
b = -1
c = 1
e=len(xyderivzip)
for d in xyderivzip:
    B=xyderivzip[b]
    C=xyderivzip[c]
    if d[0] == xcoordlist[0]:
        if d[2] > 0:
            if d[1] < C[1]:
                print((d[0],round(d[1],2)),"is a local min")
            elif d[1] > C[1]:
                print((d[0],round(d[1],2)),"is a local max")
        zero.append((' ',d[0],'+'))
        if d[2] < 0:
            if d[1] < B[1]:
                print((d[0],round(d[1],2)),"is a local min")
            elif d[1] > B[1]:
                print((d[0],round(d[1],2)),"is a local max")
        zero.append((' ',d[0],'-'))
    elif d[0] == xcoordlist[-1]:
        if d[2] > 0:
            if d[1] < C[1]:
                print((d[0],round(d[1],2)),"is a local min")
            elif d[1] > C[1]:
                print((d[0],round(d[1],2)),"is a local max")
            zero.append(('+',d[0],' '))
        if d[2] < 0:
            if d[1] < B[1]:
                print((d[0],round(d[1],2)),"is a local min")
            elif d[1] > B[1]:
                print((d[0],round(d[1],2)),"is a local max")
            zero.append(('-',d[0],' '))
    else: 
        if B[2]*d[2] > 0:
            if d[2] > 0:
                increasinglist.append(d[0])
            elif d[2] < 0:
                decreasinglist.append(d[0]) 
        elif B[2]*d[2] <= 0:
            extremalist.append((d[0], d[1]))
            if B[2] < 0 and C[2] < 0:
                print((d[0],round(d[1],2)),"is just a 0")
            elif B[2] < 0 and C[2] > 0:
                print((d[0],round(d[1],2)),"is a local min")
                increasinglist.append(d[0])
            elif B[2] > 0 and C[2] < 0:
                print((d[0],round(d[1],2)),"is a local max")
                decreasinglist.append(d[0])
            if B[2] < 0:
                before = '-'
            elif B[2] > 0:
                before = '+'
            if C[2] < 0:
                after = '-'
            elif C[2] > 0:
                after = '+'
            if d[2] == 0:
                zero.append((before,d[0],after))
            elif B[2] != 0 and C[2] !=0:
                zero.append((before,(B[0]+d[0])/2,after))
    b+=1
    c+=1
    if c == e:
        c=0

#print(zero)

incstart = []
incend = []
decstart = []
decend = []
for d in zero:
    if d[0] == '+':
        incend.append(d[1])
    elif d[0] == '-':
        decend.append(d[1])
    if d[2] == '+':
        incstart.append(d[1])
    elif d[2] == '-':
        decstart.append(d[1])
        
#print(incstart)
#print(incend)
#print(decstart)
#print(decend)
if len(incstart) == 0:
    print("your function is never increasing.")
else:
    print("Your function is increasing from:")
    for d in incstart:
        m = incstart.index(d)
        print(d,"to",incend[m])

if len(decstart) == 0:
    print("Your function is never decreasing.")
else:
    print("Your function is decreasing from:")
    for d in decstart:
        m = decstart.index(d)
        print(d,"to",decend[m])    

'''   

                                                    # This creates list of the y+0.001 and y-0.001 values to use
                                                        # in the symmetric differnce quotient to find the 
                                                            #second derivatives. 
#second derivatives
ycoordlista=[]                              
for r in xcoordlist:
    x=r+0.002
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlista.append(y)
#print(ycoordlista)

ycoordlistb=[]                              #This will find the y-.001 value for the symmetric differnce quotient. 
for r in xcoordlist:
    x=r-0.002
    Locfunction=function.lower()
    y=eval(Locfunction)
    ycoordlistb.append(y)
#print(ycoordlistb)

derivlista=[]                                #This makes a list of the derivatives, and a rounded list                                 #of the derivatives. 
for s in range(intervalnum):
    deriva  = ((ycoordlista[s])-(ycoordlist[s]))/(2*0.001)
    derivlista.append(deriva)
#print (derivlista)

derivlistb=[]                                #This makes a list of the derivatives, and a rounded list                                 #of the derivatives. 
for s in range(intervalnum):
    derivb  = ((ycoordlist[s])-(ycoordlistb[s]))/(2*0.001)
    derivlistb.append(derivb)
#print (derivlistb)

    
deriv2list=[]
deriv2list1=[]
for s in range(intervalnum):
    deriv2  = ((derivlista[s])-(derivlistb[s]))/(2*0.001)
    deriv2list1.append(round(deriv2,2))
    deriv2list.append(deriv2)
#print (deriv2list)
print(deriv2list1)
'''
y2coordlist1=[]
for d in derivlist:
    y2coordlist1.append(d+0.001)
    
y2coordlist2=[]
for d in derivlist:
    y2coordlist2.append(d-0.001)



y2coordlist1=[(x+0.001) for x in derivlist1]
print(y2coordlist1)
y2coordlist2=[(x-0.001) for x in derivlist1]
print(y2coordlist2)
'''
xcoordlista=[(x+0.001) for x in xcoordlist]
#print(xcoordlista)
xcoordlistb=[(x-0.001) for x in xcoordlist]
#print(xcoordlistb)

derivlista=[]                                #This makes a list of the derivatives, and a rounded list
derivlista1=[]                                   #of the derivatives. 
for s in range(intervalnum):
    deriva  = ((ycoordlist1[s]+0.001)-(ycoordlist1[s]-0.001))/(2*0.001)
    #derivlista1.append(round(deriva,2))
    derivlista.append(deriva)
#print (derivlista1)
print (derivlista)

derivlistb=[]                                #This makes a list of the derivatives, and a rounded list
derivlistb1=[]                                   #of the derivatives. 
for s in range(intervalnum):
    derivb  = ((ycoordlist2[s]+0.001)-(ycoordlist2[s]-0.001))/(2*0.001)
    #derivlistb1.append(round(derivb,2))
    derivlistb.append(derivb)
#print (derivlistb1)
print (derivlistb)
    
deriv2list=[]
deriv2list1=[]
for s in range(intervalnum):
    deriv2  = ((derivlista[s])-(derivlistb[s]))/(2*0.001)
    deriv2list1.append(round(deriv2,2))
    deriv2list.append(deriv2)
#print(deriv2list1)
#print (deriv2list)

                                                    #This creates a list with the x and y coordinates, 
                                                        #first derivatives and second derivatives. 
xyderiv2zip=list(zip(xcoordlist, ycoordlist, derivlist, deriv2list))
#print(xyderiv2zip)

                                                    #These loops check to see where the second derivative is zero,
                                                        #positive or negative in order to determine POI and concave
                                                            #up and down intervals. 
'''

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
    if a: 
        print("There is a ALSO a point of inflection at x=", asymptote, ".")
print (poilist)
print (concaveuplist)
print (concavedownlist)
# concave up interval(s)
concaveuplist=[]
for d in xyderiv2zip:
    if d[3]>=0:
        concaveuplist.append(d[0])
print (concaveuplist)
lengthconcaveup=len(concaveuplist)
print(lengthconcaveup)
#print('Your function is concave up from' concaveuplist[0] 'to' concaveuplist[lengthconcaveup])
#concave down interval(s)
concavedownlist=[]
for d in xyderiv2zip:
    if d[3]<=0:
        concavedownlist.append(d[0])
print (concavedownlist)
lengthconcavedown=len(concavedownlist)
#print('Your function is concavedown from' concavedownlist[0] 'to' concavedownlist[lengthconcavedown])

                                    #This is the code for the graphs of the function and derivative.
'''                                 #This defines the colors.
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
#print(graphycoords)
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
    
points = CircleAsset(5, thinline, purple)
                                     #This defines the coordinates to graph the derivative.
graphy3coords=[y*-1 for y in deriv2list]
x2coords = xcoordlist
y2coords = graphy2coords
xy2coords=list(zip(x2coords,y2coords))
                                     #This graphs the derivative.
for i in xy2coords: 
    Sprite(points, ((25*(i[0]+20)),(25*(i[1]+10))))

myapp = App()
myapp.run()
