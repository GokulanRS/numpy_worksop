#write a program to find the factorial of a nummber
def fac(num):
    if(num==1):
        return 1
    else:
        return num * fac(num-1)

num=int(input("Enter any number"))
x=fac(num)
print(x)
