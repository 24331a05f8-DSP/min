
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if a>=b and a>=c :
    maxp=a
elif b>=a and b>=c :
    maxp=b
else :
    maxp=c
if a<=b and a<=c :
    minp=a
elif b<=a and b<=c :
    minp=b
else :
    minp=c
print("max=",maxp)      
print("min=",minp)
