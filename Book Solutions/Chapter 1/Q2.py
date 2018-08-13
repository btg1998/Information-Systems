import sys
try:
    i=int(input("enter a number or Enter to finish: "))
except:
    print(" -_- ")
    sys.exit(0)
l=[]
while True:
    s=int(i)
    l.append(s)
    try:
        i=int(input("enter a number or Enter to finish: "))
    except:
        break
print("numbers: ",l)
c=len(l)
su=0
hi=l[0]
low=l[0]
for i in l:
    su=su+i
    if i>hi:
        hi=i
    if i<low:
        low=i
avg=su/c
print("count = ",c," sum = ",su," lowest = ",low," highest = ",hi," mean = ",avg)

