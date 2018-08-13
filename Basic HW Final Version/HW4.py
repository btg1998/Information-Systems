def middle(a):
    ans=[]
    for i in range(1,len(a)-1):
        ans.append(a[i])
    return ans
print("Enter list: ")
a = [int(x) for x in input().split()]
print(middle(a))
