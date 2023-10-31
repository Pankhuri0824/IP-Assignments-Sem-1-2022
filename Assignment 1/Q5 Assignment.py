angle=int(input("Please enter the angle of elevation:"))
distance=int(input("PLease enter the distance to the pole:"))
radian=((3.14)/180)*angle

#need to compute tan0=height/distance
def factorial(f):
    for i in range (1,f):
        f=f*i
    return f
def sin(x):
    sinx = 0
    for i in range (0,50):
        sinx=sinx+(((-1)**i)*(x**(2*i+1))/(factorial(2*i+1)))
    return sinx
sinx=sin(radian)
cosx=((1-(sin(radian))**2))**(1/2)
tanx=sinx/cosx
height=tanx*distance
tip=height/sinx
print("Height of the pole is:",height)
print("Distance to the tip of the pole",tip)
