a=1
b=3
while a<=5:
    c=int(input("enter the number"))
    a=a+1
    if c==b:
        print("you have guessed it right")
        break
else:
    print("you have loss your chances")