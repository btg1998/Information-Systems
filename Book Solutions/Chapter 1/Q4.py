import random
import sys
ar=['a','an','the','another']
ve=['sang', 'ran','jumped']
ad=['loudly', 'quietly', 'well', 'badly']
sub=['cat','dog', 'man', 'woman']
de=5
try:
    de=int(input())
except:
    de=5
if 1<de<10:
    pass
else:
    print("Not a number between 1 and 10...Exiting.")
    sys.exit(0)
while de>0:
    ans=''
    i=random.randint(0,1)
    if i==0:
        ans=ans+random.choice(ar)
        ans=ans+" "
        ans=ans+random.choice(sub)
        ans=ans+" "
        ans=ans+random.choice(ve)
        ans=ans+" "
        ans=ans+random.choice(ad)
        print(ans)
    elif i==1:
        ans=ans+random.choice(ar)
        ans=ans+" "
        ans=ans+random.choice(sub)
        ans=ans+" "
        ans=ans+random.choice(ve)
        print(ans)
    de=de-1
