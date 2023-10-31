l=[]
while True:
    n=list(map(str,input().split()))
    if n==[]:
        break
    else:
        l.append(n)

c1=[1,2,4]
c2=["A+","A","A-","B","B-","C","C-","D","F"]
CR=True #credit
GR=True #grade
CO=True #Course name

for i in range (len(l)):
    if int(l[i][1]) not in c1: #credit no.
        print("incorrect credit entered")
        CR=False
    if l[i][2] not in c2: #grade
        print("incorrect grade entered")
        GR=False
    if (l[i][0]).isalnum():  #course name
        if l[i][0][:3].isalpha() and l[i][0][3:].isnumeric():
            pass
        elif l[i][0][:4].isalpha() and l[i][0][4:].isnumeric():
            pass
        else:
            print("improper course no")
            CO=False
    elif not (l[i][0]).isalnum():
        print("improper course no")
        CO=False

if CR==True and GR==True and CO==True:
    grades={"A+":10,"A":10,"A-":9,"B":8,"B-":7,"C":6,"C-":5,"D":4,"F":2}
    def sgpa(l):
        credits=0
        a1=0
        for i in range (len(l)):
            course=str(l[i][0])
            credit=int(l[i][1])
            grade=grades[l[i][2]]
            print(f'{course}:{l[i][2]}')
            a=credit*grade
            a1+=a
            credits+=credit
        sgpa=a1/credits
        return sgpa 

    print("Your SGPA is:",sgpa(l))

