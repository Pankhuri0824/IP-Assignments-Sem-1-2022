##create output files for running 

class Course:
    def __init__(self,a,b,c,d):
        self.name=a
        self.credits=b
        self.assesment=c
        self.policy=d

class Student:
    def __init__(self,roll,ms,es):
        self.rollno=roll
        self.midsem=int(ms)
        self.endsem=int(es)
        self.total=(int(ms)+int(es))

a="IP"
b=4
c=[("midsem",40),("endsem",60)]
d=[80,65,50,40,30]
x=Course(a,b,c,d)

f=open("./Q4.txt")
data=[]
tot=[]
for line in f:
    l=line.split()
    s=Student(l[0],l[1],l[2])
    data.append(s)
    tot.append(s.total)

###
# A>80....80>B>65....65>C>50....50>D>40...40>F
def grading1(l):
    # A>80....80>B>65....65>C>50....50>D>40...40>F
    A=[]
    B=[]
    C=[]
    D=[]
    for i in l:
        if 82>i>78:
            A.append(i)
        elif 67>i>63:
            B.append(i)
        elif 52>i>48:
            C.append(i)
        elif 42>i>38:
            D.append(i)
    A.sort()
    B.sort()
    C.sort()
    D.sort()
    grade=[A,B,C,D]
    cutoff={}
    gr={0:"A",1:"B",2:"C",3:"D"}
    a=0
    for k in grade:
        a1=gr[a]
        g={}
        if k==[]:
            cutoff[a1]=d[a]
        else:
            if len(k)>1:
                for i in range (0,len(k)-1):
                        g[k[i],k[i+1]]=abs(k[i]-k[i+1])
                l=list(g.values())
                m=max(l)
                val=[i for i in g.keys() if g[i]==m]
                for i in val:
                    s=0
                    for y in range (len(i)):
                        s+=i[y]
                cuto=s/2
                cutoff[a1]=cuto
            else:
                for i in k:
                    cutoff[a1]=i
        a+=1
    return cutoff
cutoff=grading1(tot)
# policy = [80,65,50,40,30]
keys=list(cutoff.keys())
keys.append("F")
values=list(cutoff.values())
values.append(0)

def grading(n):
    grdes=["A","B","C","D","F"]
    if n>=values[0]:
        return grdes[0]
    elif values[0]>n>=values[1]:
        return grdes[1]
    elif values[1]>n>=values[2]:
        return grdes[2]
    elif values[2]>n>=values[3]:
        return grdes[3]
    elif values[3]>n>=values[4]:
        return grdes[4]
###
t=True
while t:
    n=(input("Enter command:"))
    if n=="":
        t=False
        print("Program Terminated")
        break
    n=int(n)
    if n==1: 
        print("Course name:",x.name)
        print("Credits:",x.credits)
        print("Assesment", f' 1) Midsem:{x.assesment[0][1]}, 2)Endsem: {x.assesment[1][1]}')
        print("Grade cutoffs for the course are as follows:")
        for i in range (len(cutoff)+1):
            if i==0:
                print(f'{keys[i]} : {values[i]}-100')
            else:
                print(f'{keys[i]} : {values[i]}-{values[i-1]}')
        key=list(data[i-1].rollno for i in range (len(data)))  #Roll numbers
        ga,gb,gc,gd,gf=0,0,0,0,0
        for i in range (len(data)):
            x=grading(tot[i])
            if x=="A":
                ga+=1
            elif x=="B":
                gb+=1
            elif x=="C":
                gc+=1
            elif x=="D":
                gd+=1
            elif x=="F":
                gf+=1
        lis=[ga,gb,gc,gd,gf]
        grdes=["A","B","C","D","F"]
        print("Grading summary is as follows:")
        for i in range (5):
            print(f"Number of {grdes[i]}'s : {lis[i]}")

        ####
    elif n==2:
        f1=open("./Q4Output.txt","w")
        for i in range (len(data)):
            f1.write(f'Roll Number :{data[i].rollno}, Total marks:{data[i].total}, Grade: {grading(data[i].total)}'+"\n") 
    elif n==3:
        n1=int(input("Enter Roll number:"))
        print(f'Marks by assesments : 1)Midsem:{data[n1-1].midsem}, 2)Endsem:{data[n1-1].endsem}')
        print("Total Marks:",data[n1-1].total)
        print("Final grade",grading(data[n1-1].total))

