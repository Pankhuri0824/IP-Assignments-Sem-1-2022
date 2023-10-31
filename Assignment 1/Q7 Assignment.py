cost=int(input("Cost of laptop:"))
allowance=20000 
sf=0.1 #saving fraction
r=0.005 #monthly rate of interest
constant_saving=0.1*allowance
saving=allowance*0.1
time=0
while saving<=cost:
    CA=saving*((1+(r))**1) # because t in formula is once, since interest is compounded monthly
    if time==0:
        saving=CA
    else:
        saving=CA+constant_saving
    time+=1
if saving==cost:
    time=time
elif saving<cost:
    time+=1
print("Number of months needed:",time)
print("Savings still left:",saving-cost)


