d={}
file=open("./Q2.txt")

def corr(di):
    for name in di.keys():
        dolphin=[]
        l_temp=[]
        for x in range(1,len(di[name]["status"])):
            dolphin.append(x)

        for i in dolphin:
            if "ENTER"==di[name]["status"][i]:
                if di[name]["status"][i]==di[name]["status"][i-1]:
                    l_temp.append(i)
            elif "EXIT"==di[name]["status"][i]:
                if di[name]["status"][i]==di[name]["status"][i-1]:
                    l_temp.append(i-1)

        for x in l_temp[::-1]:
            for temp in di[name].keys():
                d[name][temp].pop(x)
    
    return di
def pants(name,ab,abc,abcd):
    return f'{name}, {ab}, {abc}, {abcd}'
    
def fin(name):
    lis=[]
    if name in d.keys():
        for i in [damn for damn in range(len(d[name]["gateno"]))]:
            lis.append([d[name]["status"][i],d[name]["gateno"][i],d[name]["time"][i]])
    return lis


####file to dictionary####
file.readline()

for l in file:
    x=l.strip('\n').split(",")
    if x[0] not in d.keys():
        d[x[0]]={}
        d[x[0]]["status"],d[x[0]]["gateno"],d[x[0]]["time"]=[],[],[]

    d[x[0]]["status"].append(x[1])
    d[x[0]]["gateno"].append(int(x[2]))
    d[x[0]]["time"].append(x[3].strip())

d=corr(d)
t=True
while t:
    x=int(input("Enter command:"))
    if x==4:
        t=False
        print("Program Terminated")
        break
    else:
        if x==1:
          nam=input("enter the name:")
          tm=input("time:")
          r=fin(nam)
          r.sort(key= lambda a: a[2])
          for xd in range(len(r)-1):
              f=open("Q2Output1.txt","w")
              if tm<r[xd+1][2] and tm>=r[xd][2]:
                  flag=''
                  if "EXIT"==r[xd][0].strip():
                      flag='NOT'
                  printout=f'{str(r)}\nCURRENTLY {flag} IN THE CAMPUS'
                  f.write(printout)
                  break
              elif r[0][0].strip()=="EXIT" and tm<r[0][2]:
                  f.write(f'{str(r)}\nCURRENTLY IN THE CAMPUS')
                  break
        elif x==2:
            exit_li=[]
            enter_li=[]
            start=input("start: ")
            end=input("end: ")
            for name in d.keys():
                for m in range(len(d[name]['time'])):
                    if d[name]['time'][m]>start and d[name]['time'][m]<end and d[name]['status'][m]==" ENTER":
                        enter_li.append(pants(name,d[name]['status'][m],d[name]['gateno'][m],d[name]['time'][m]))
                for n in range(len(d[name]['time'])):
                    if d[name]['time'][n]>start and d[name]['time'][n]<end and d[name]['status'][n]==" EXIT":
                        exit_li.append(pants(name,d[name]['status'][n],d[name]['gateno'][n],d[name]['time'][n]))
                        
            f=open("Q2Output2.txt","w")        
            f.write("ENTER:\n")
            enter_print=''
            exit_print=''
            for m in enter_li:
                enter_print+=str(m)+'\n'
            f.write(enter_print)
            f.write("EXIT:\n")
            for m in exit_li:
                exit_print+=str(m)+'\n'
            f.write(exit_print)

        elif x==3:
            gate=int(input("enter gate number:"))
            for name in d.keys():
                print(name)
                entcount=0
                extcount=0
                for i in range(len(d[name]["gateno"])):
                    guest=d[name]["gateno"][i]
                    guest1=d[name]["status"][i]
                    if guest==gate and guest1.strip()=="ENTER":
                        entcount+=1
                    if guest==gate and guest1.strip()=="EXIT":
                        extcount+=1
                print(f'entry:{entcount}\nexit:{extcount}')
            
            
          
