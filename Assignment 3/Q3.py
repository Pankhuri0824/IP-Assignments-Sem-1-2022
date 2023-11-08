##CREATE OUTPUT FILES BEFORE RUNNING THE CODE

import random
l=["./Q3File1.txt","./Q3File2.txt"]
counter=0
for file in l:
    name=f'{file}'
    f=open(file,"r")
    #F1 
    u=[]
    total=[]
    for line in f:
        a=line.split()
        for i in a:
            total.append(i)
            if i not in u:
                u.append(i)
    F1=(len(u))/len(total)
    #F1 CHECKER
    # print("total words:",len(total))
    # print("Unique words:",len(u))
    # print("F1 is:",F1)
    #F2 - will use unique words list u for frequency
    d={}
    for i in u:
        n=0
        for k in total:
            if i==k:
                n+=1
        d[i]=n
    a=[i for i in d.values()]
    a.sort(reverse=True)
    # print(a) #FREQUENCIES OF ALL UNIQUE WORDS
    l=[]
    top=[]
    for i in range (0,5):
        n=a[(i)]
        t=[k for k in d.keys() if d[k]==n]
        top.append(t)
        l.append(n)
    l=set(l)
    l=list(l)
    most=0
    for i in l:
        for k in u:
            if d[k]==i:
                most+=i #MOST WORDS COMBINED FREQUENCY
    F2=most/len(total)
    # F2 CHECKER
    # print(F2) 

    #F3
    f.close()
    f=open("./Q3File1.txt")
    a=f.read()
    a=a.split(".")
    s=[]
    for line in a:  #splits sentences
        x=line.split("\n")
        x=" ".join(x)
        s.append(x)
    # print(s)
    sen=0
    for i in s:
        i=i.split()
        if len(i)>35 or len(i)<5:
            sen+=1
    # print(sen,len(s))
    F3=sen/len(s) 
    # print(F3)

    #F4
    

    #F5
    if len(total)>750:
        F5=1
    else:
        F5=0

    ns=4+(F1*6)+(F2*6)-(F3)-(F5)

    new=[]
    for x in range (5):
        i=random.randint(0,len(total))
        word=total[i-1]
        new.append(word)
    mostused=[]
    t=True
    while t:
        for i in top:
            if len(i)==1:
                if len(mostused)==5:
                    t=False
                    break
                else:
                    mostused.append(i[0])
            else:
                if len(mostused)==5:
                    t=False
                    break
                else:
                    for k in range (len(i)):
                        mostused.append(i[k])
                        if len(mostused)==5:
                            t=False
                            break
    
    
    f1=open("./Q3Scores.txt","w")
    s=f'''
    Filename:" {name}
    Score is: {ns}
    Five most used words are:{mostused}
    Five random words :{new} '''
    if counter==0:
        s1=s
        f1.write(s)
    elif counter==1:
        f1.write(f'''{s1}


    {s}''')
    counter+=1

    
