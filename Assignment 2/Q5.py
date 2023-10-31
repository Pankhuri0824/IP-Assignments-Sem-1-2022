t=True
l=[]
while t:
    a=tuple(map(int,input("Enter coordinates:").split()))
    if a==():
        t=False
    else:
        l.append(a)
m1=[]
n=len(l) # number of rows 
for i in range (n):
    b=1
    coor=[]
    coor.append(l[i][0])
    coor.append(l[i][1])
    coor.append(b)
    m1.append(coor)
cx=int(input("enter scaling parameter cx:"))
cy=int(input("enter scaling parameter cy:"))
m2=[[cx,0,0],[0,cy,0],[0,0,1]]
#matrix multiplication 
m3=[]
for r in range (n): #rows of m1
    row=[]
    for c in range (3): #coloumns of m2
        s=0
        for i in range (3): 
            x=m1[r][i]*m2[i][c]
            s+=x
        row.append(s)
    m3.append(row)
#m3 is the required matrix
print("Required coordinates are:",end="")
for i in range (len(m3)):
    print(f'({m3[i][0]},{m3[i][1]})',end=",")

