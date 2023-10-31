pop=[50,1450,1400,1700,1500,600,1200]
total=0
new=0
for i in (pop):
    total+=i
print("Current total population of the world is:",total)
g=2.5/100
y=0
og=0
total_pop=0
for i in pop:
    while True:
        i=i-(i*g)
        g=g-0.4/100
        total_pop+=i
        y=y+1
        if total_pop<og and y>2:
            break
        og=total_pop
    g=g-0.1

print(y)


    
    
        




    
    


    


    