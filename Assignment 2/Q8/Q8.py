n=int(input("Till where you would like to check:"))
f=open("./Q8Input.txt","r")
#init_importance, overall importance, the set of URLs it accesses,
d={}
s1=""
s2=""
for line in f:
    line=line.strip("\n")
    a=line.split(",") #a[0] is key url 
    s1=a[0]
    d[s1]={}
    b=a[1].split(":") #b[0] is importance
    s2=b[0]
    d[s1]["importance"]=float(s2)
    c=b[1].split()
    d[s1]["su"]=c

dict={}
for i in d.keys():
    dict[i]={}
    v=i
    imp=d[i]["importance"]
    for k in set(d[v]["su"]):
        imp=imp
        lg=len(set(d[v]["su"]))
        val=imp/lg
        dict[v][k]=val

d1={}
l=[]
for i in dict.values():
    for k in i.keys():
        if k not in d1:
            d1[k]=i[k]
        else:
            d1[k]+=i[k]

mx=max(d1.values())
ans=[k for k in d1.keys() if d1[k]==mx]
l=[i for i in d1.values()]
l.sort(reverse=True)
for x in range (n):
    a=[k for k in d1.keys() if d1[k]==l[x]]
    print(f'{x}. {str(a[0])} {l[x]}')



#FORMULA - IMPORTANCE/ NO. OF UNIQUE TERMS
