i=0
sum=0
c=int(input("enter first number"))
while i<c:
    a=int(input("enter second number"))
    sum=sum+a
    i=i+1
total_sum=sum
avg=total_sum//c
print(avg) 
if avg%5==0:
    print("multiple of 5")
else:
    print("not multiple of 5")       