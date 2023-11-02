f=open("./Q3yearbook.txt","r")
l=[]
d={}
for line in f:
    line=line.strip('\n')
    a=line.split(",")
    l.append(a)

for i in l:
    b={}
    if len(i)==1:
        b=i[0].strip(":")
        d[b]={}
        v=b
    elif len(i)==2:
        d[v][i[0]]=int(i[1])  

sign=[]
dict={}
for i in d.keys():
    sum=0   
    for k in d[i].values():
        sum+=k
    sign.append(sum)
    dict[i]=sum
m=max(sign)
n=min(sign)
max=[k for k in dict if dict[k]==m]
print(f'Maximum number of signatures were in {max}s yearbook')
min=[k for k in dict if dict[k]==n]
print(f'Minimum number of signatures were in {min}s yearbook')
