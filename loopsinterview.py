a=int(input("enter the number"))
i=1
sum=0
while i<=a:
    if i%5==0 and i%7==0:
        sum=sum+i
    i=i+1
print(sum)    