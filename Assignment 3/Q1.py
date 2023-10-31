'''Question 1.
Print the pattern given below using recursion - no loops are allowed. You are given a value n -
print a diamond which will have 2n-1 rows, and 2n columns, as shown in the figure. (In the top row print 
n+n stars, in the next (n-1) stars on left and right and 2 blanks in the middle, and so on till you have 
1 star each on left and right; then you reverse this).'''
n=int(input("Enter input:"))
r=2*n-1
c=2*n
global f
f=True
def pattern(n):
    d=c-(2*n)
    print(("* "*n)+("  "*d)+(" *"*n))
    global f
    while f:
        n=n-1
        if n==0:
            f=False
            break
        pattern(n)
pattern(n)

f1=True
def mirror(n):
    co=(int(c/2)-(n))+1
    d=d=c-(co*2)
    if co!=1:
        print(("* "*co)+("  "*d)+(" *"*co))
    global f1
    while f1:
        n=n-1
        if n==0:
            f1=False
            break
        mirror(n)
mirror(n)
