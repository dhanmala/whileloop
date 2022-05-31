n=int(input("enter number"))
rev=0
c=n
while c>0:
    a=c%10
    rev=rev*10+a
    c=c//10
print(rev)
if n==rev:
    print("palindrome")
else:
    print("not palindrome")    