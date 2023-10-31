l=[]
x=5.0
y=5.0
n=0
while True:
    a=int(input())
    l.append(a)
    n+=a
    if a<=0:
        print("Journey has ended")
        break
def north(n):
    global x
    global y
    y+=n
    return(x,y)
def south(n):
    global x
    global y
    y-=n
    return(x,y)
def east(n):
    global x
    global y
    x+=n
    return(x,y)
def west(n):
    global x
    global y
    x-=n
    return(x,y)
for i in range(len(l)):
    if l[i]<=0:
        pass
    elif 0<l[i]<=25:
        #north
        north(l[i])
    elif 25<l[i]<=50:
        #south
        south(l[i])
    elif 50<l[i]<=75:
        #east
        east(l[i])
    elif l[i]>75:
        #west
        west(l[i])
print("Final coordinates are:",x,y)
print("Total distance is:",n)
Sld=((x-5)**2+(y-5)**2)**(1/2)
print("Straight line distance:",Sld)

