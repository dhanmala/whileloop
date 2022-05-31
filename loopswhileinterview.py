n=int(input("enter the number"))
rev=0
c=n
while c>0:
    a=c%10
    rev=rev*10+a
    c=c//10
print(rev)
