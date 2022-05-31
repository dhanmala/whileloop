a=1
b=4
c=7
d=5
while a<=5:
    e=int(input("enter the number"))
    a=a+1
    if e<b:
        print("number enterby you is small")
    elif e>c:
        print("number enter by you is greater try one more time")
    elif e==d:
        print("wow you gussed the correct number")
        break
else:
    print("none")            