def ack(m,n):
    if m==0:
        return (n+1)
    elif m>0 and n==0:
         return ack((m-1),1)
    elif m>0 and n >0:
        l=ack(m,(n-1))
        return ack((m-1),l)
m=int(input("Enter m:"))
n=int(input("Enter n:"))
print(ack(m,n))
