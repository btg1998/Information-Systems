def cumsum(a):
    ans=[]
    ans.append(a[0])
    for i in range(1,len(a)):
        t=0
        for j in range(i+1):
            t=t+a[j]
        ans.append(t)   
    print(ans)
print("Enter the list: ")
a = [int(x) for x in input().split()]
cumsum(a)
