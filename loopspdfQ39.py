i=1
a=int(input("enter the number"))
while i<=a:
    b=int(input("enter second number"))
    if b==a:
        print("you guess right")
        i=i+1
        break
else:
    print("you guess wrong")    