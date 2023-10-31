a=int(input())
for i in range(1,a+1):
    #left straight
    for j in range(i):
        print("*",end="")
    #right straight
    for j in range(i,a):
        print(" ",end="")
    #left straight
    for k in range(i,a):
        print(" ",end="")
    #right straight
    for k in range(i):
        print("*",end="")
    print()
