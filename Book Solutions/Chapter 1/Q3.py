import random
ar=['a','an','the','another']
ve=['sang', 'ran','jumped']
ad=['loudly', 'quietly', 'well', 'badly']
sub=['cat','dog', 'man', 'woman']
for i in range(5):
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
