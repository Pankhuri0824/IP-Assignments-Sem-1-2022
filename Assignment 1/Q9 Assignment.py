import math
a,b,c,d=10,1.05,1,1.06
p=1
def demand(a,b,p):
    x=a-b*p
    return math.exp(x)
def supply(c,d,p):
    y=c+d*p
    return math.exp(y)
def check(a,b,c,d,p):
    while True:
        x=demand(a,b,p)
        y=supply(c,d,p)
        if x==y:
            print("Equilibrium:",x)
            return
        if y>x:
            print("No solution is possible")
            print("Demand is:",x)
            print("Supply is",y)
            print("Price is",p)
            return
        p=p*(1.05)
check(a,b,c,d,p)

