bnum=int(input("enter the binary number"))
dnum=0
i=1
while bnum!=0:
    rev=bnum%10
    bnum=bnum//10
    dnum=dnum+rev*i
    i=i*2
print(dnum)