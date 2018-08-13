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
for i in range(1,c):
    j=i-1
    key=l[i]
    while((j>=0)and(key<l[j])):
        l[j+1]=l[j]
        j=j-1
    l[j+1]=key
print(l)
if c%2!=0:
	med=l[int(c/2)]
else:
	med=((l[int(c/2)]+l[int(c/2)-1])/2)
print("count = ",c," sum = ",su," lowest = ",low," highest = ",hi," mean = ",avg," median = ",med)
