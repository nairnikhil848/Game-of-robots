s=input("enter the input/Only give input from 0-9 or .\n")
global num
num=0
global a
a=0
global flag
flag = bool
for i in s:
    if(i.isdigit()):
        if(a==0):
            a=int(i)
            print(a)
        else:
            b=int(i)
            print(a+b)
            if(a+b<=num):
                a=b
                num=0
            else:
                flag=False
    else:
        num=num+1
if(flag==False):
    print("NOTSAFE")
else:
    print("SAFE")