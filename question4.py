#write a program to find the sum of digits of a given number'
x=int(input("Enter any number"))
sum=0
while (x!=0):
    sum=sum+x%10
    x=x//10
print(sum)
