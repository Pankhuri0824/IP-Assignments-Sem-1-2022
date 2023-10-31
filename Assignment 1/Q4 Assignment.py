import math
a,b=float(input()),float(input())
s=0
t=a
dx=0.25
def c(t):
    first=2000*(math.log((140000)/(140000-2100*t)))
    second=9.8*t
    y=first-second
    return y
while t<b:
    s+=c(t+dx/2)*dx
    t+=dx
print(s)