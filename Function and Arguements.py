import sys
import math

def area(shape="2-d",*args,**kwargs):
    keys=sorted(kwargs.keys())
    if shape=="2-d":
        print("Please enter a valid choice...Exitting")
        sys.exit(0)
    print("Hello ",args," The area you asked for is: ")
    if shape=="S":
        print(kwargs[keys[0]]*kwargs[keys[0]])
    elif shape=="T":
        print(0.5*(kwargs[keys[0]]+kwargs[keys[1]])*kwargs[keys[2]])
    elif shape=="C":
        print(math.pi*kwargs[keys[0]]*kwargs[keys[0]])
    elif shape=="Re":
        print(kwargs[keys[0]]*kwargs[keys[1]])
    elif shape=="Rh":
        print(0.5*kwargs[keys[0]]*kwargs[keys[1]])
    



name=input("Enter your name: ")
ch=int(input("Enter 1-Circle 2-Rectangle 3-Square 4-Rhombus 5-Trapezium"))


if (ch==3):
       n=int(input("Enter Side: "))
       area("S",name,s=n)
elif ch==2:
       l=int(input("Enter length: "))
       b=int(input("Enter breadth: "))
       area("Re",name,le=l,br=b)
elif ch==1:
       n=int(input("Enter Radius: "))
       area("C",name,r=n)
elif ch==4:
    d1=int(input("Enter diagonal 1: "))
    d2=int(input("Enter diagonal 2: "))
    area("Rh",name,e=d1,f=d2)
elif ch==5:
    d1=int(input("Enter parallel side 1: "))
    d2=int(input("Enter parallel side 2: "))
    ht=int(input("Enter Height: "))
    area("T",name,a=d1,b=d2,c=ht)
else:
    print(area())
