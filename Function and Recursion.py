import sys

def fact1(n):
    pdt=1
    for i in range(1,n+1):
        pdt=pdt*i
    return pdt

def fact2(n):
    if n==1:
        return 1
    else:
        return n*fact2(n-1)
    
fact3 = lambda n: n==0 and 1 or n*fact3(n-1)

n=int(input("Enter an integer to find out it's factorial: "))
if(n<0):
    print("Please enter a positive integer...Exiting")
    sys.exit(0)
ch=int(input("Enter 1 to use function without recursion 2 to use function with recursion and 3 to use lambda function: "))
if(ch==1):
    print(fact1(n))
elif(ch==2):
    print(fact2(n))
elif(ch==3):
    print(fact3(n))
else:
    print("Invalid Choice....Exiting")
    sys.exit(0)
    

