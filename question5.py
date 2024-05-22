#write a program to find if the given number is prime no or not
num = int(input("Enter a number: "))

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print("NOT PRIME")
           break
   else:
       print("PRIME")
else:
   print("NOT PRIME")
