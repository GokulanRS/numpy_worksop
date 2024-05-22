# find if the given number is a palindrome or not?
x=int(input("Enter any number"))
y=x
rev=0
while(y!=0):
    rev=(rev*10)+(y%10)
    y=y//10
if(rev==x):
    print("PALINDROM")
else:
    print("NOT PALINDROM")
