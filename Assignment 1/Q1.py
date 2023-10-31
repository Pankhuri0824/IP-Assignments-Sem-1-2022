n=int(input())
def tens(a):
    if a==0:
        pass
    elif a==1:
        pass
    elif a==2:
        t="Twenty"
    elif a==3:
        t="Thirty"
    elif a==4:
        t="Forty"
    elif a==5:
        t="Fifty"
    elif a==6:
        t="Sixty"
    elif a==7:
        t="Seventy"
    elif a==8:
        t="Eighty"
    elif a==9:
        t="Ninety"
    return t
def ones(b):
    if b==0:
        o=""
    elif b==1:
        o="one"
    elif b==2:
        o="two"
    elif b==3:
        o="three"
    elif b==4:
        o="four"
    elif b==5:
        o="five"
    elif b==6:
        o="six"
    elif b==7:
        o="seven"
    elif b==8:
        o="eight"
    elif b==9:
        o="nine"
    return o
a=n//10
b=n%10
if n<10 or n>=20:
    print(tens(a),ones(b))
else:
    if n==10:
        print("Ten")
    elif n==11:
        print("Eleven")
    elif n==12:
        print("Twelve")
    elif n==13:
        print("Thirteen")
    elif n==14:
        print("Fourteen")
    elif n==15:
        print("Fifteen")
    elif n==16:
        print("Sixteen")
    elif n==17:
        print("Seventeen")
    elif n==18:
        print("Eighteen")
    elif n==19:
        print("Nineteen")

