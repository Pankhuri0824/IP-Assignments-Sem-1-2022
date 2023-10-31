menu=[("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70),
      ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]
 
for i in range (len(menu)):
    print((i+1),menu[i][0],((30-(len(menu[i][0])))*"-"),"₹",menu[i][1])       #serial no is i+1 - IMP
 
order=[]
while True:
    l=list(map(int,input().split()))
    if l==[]:
        break
    else:
        order.append(l)

total=0
q=0
for k in range (0,len(order)):
    for i in range (len(order[k])):
        if i%2==0:
            price=menu[order[k][i]-1][1] #cost
            quantity=order[k][i+1]
            sum=price*quantity
            total+=sum
            q+=quantity
            print(f'{menu[order[k][i]-1][0]},{quantity},Rs{price}')
 
print(f'TOTAL: {q} items, Rs {total}')
