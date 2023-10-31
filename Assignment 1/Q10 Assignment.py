a,b,c,d=1,(-10.5),34.5,(-35)

def mod1(a,b,c,d,x):
    x=a*(x**3)+b*(x**2)+c*x+d
    return x
def derivative(x):
    x=3*(x**2)-21*x+34.5
    return x

x0=float(input())
t=0
xox=x0
while abs(mod1(a,b,c,d,xox))>0.2:
    if t>100:
        print("root not found")
        break
    xox=xox-(mod1(a,b,c,d,xox)/derivative(xox))
    t+=1

print(xox)
